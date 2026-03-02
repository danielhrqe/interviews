| Passo | Objetivo | O Que Fazer | Frases-Chave | Armadilhas |
|-------|----------|------------|--------------|------------|
| **1. Problem** | Enquadrar problema | Tipo ML (ranking/class/reg), objetivo negócio, constraints (latência, volume, real-time vs batch) | "É um problema de X com objetivo Y. Vou definir métricas → dados → features → modelo → serving → monitoramento." | Não clarificar logado vs anon. Ignorar latência/volume. |
| **2. Metrics** | Definir sucesso | Offline (model quality) + Online (business impact) | "Offline otimizo X. Online valido com A/B usando Y." | Só falar métrica offline. Esquecer A/B. |
| **3. Data & Labels** | Construir training set | Fonte dados, definir label (explícito/implícito), split temporal | "Cada row = (query/user, item, label). Split temporal evita leakage." | Random split com dados temporais. Ignorar label delay. |
| **4. Features** | Sinal preditivo | Item, User, Context, Cross | "Features devem estar disponíveis no serving." | Criar feature que não existe online. |
| **5. Model** | Estratégia evolutiva | Baseline → XGB → LTR/Deep | "Começo simples, interpreto, depois escalo complexidade." | Ir direto para deep model. |
| **6. Serving** | Arquitetura prática | Two-stage: Retrieval → Ranking → Re-rank | "Não rankeio 500K em tempo real. Reduzo candidatos primeiro." | Esquecer latência total. |
| **7. Monitoring** | Sustentar produção | Performance, drift, feature health, latência | "Deploy sempre via A/B test." | Não falar de drift ou retraining. |

| Problema | Tipo | Pipeline | Modelo | Métrica | Deep Points | Trade-offs |
|------------|------------|----------------------------|----------------|----------------|-----------------------------|----------------------------|
| **Ranking (Anon)** | Ranking | ES (500) → Redis → XGB → Re-rank | XGBoost / LambdaMART | NDCG / CTR | Label 3>2>1>0, split temporal, cross query×item | Popularidade no cold start. Retrieval reduz latência. |
| **Preço Aluguel** | Regressão | Feature Store → XGB → Batch suggestion | XGB / Ensemble | MAPE | Label = preço final contrato. Mercado (m², oferta/demanda). | Drift → retreino mensal. Batch > realtime. |
| **RAG Contrato** | Retrieval + LLM | PDF → Chunk 512/50 → Embed → pgvector → Top-5 → LLM | Embedding + GPT | Retrieval@5 | Classifier OOS, guardrails, no PII | Custo vs qualidade LLM. |
| **Fraude** | Binary (1% pos) | Evento → Kafka → Score → Flag → Moderador | XGB + rules | Recall / PR-AUC | class_weight + threshold ~0.3, delayed label | Recall > Precision. Human-in-loop. |
| **Recomendação (Logado)** | RecSys | Histórico → Grafo U-I → Similaridade → Rank | CF + Content Hybrid | CTR / Engagement | User-Item Graph, cosine/Jaccard similarity | Cold start → content + popularidade |
| **Segmentação Inquilinos** | Clustering (unsup.) | Features → Normalizar → K-Means → K clusters → Perfis | K-Means / DBSCAN | Silhouette, Inertia (elbow) | Features: faixa preço, bairros vistos, tipo imóvel, device, horário busca. Sem label! | K pelo elbow method. Usar pra: personalizar UX, email mkt, pricing strategy por segmento |

| Conceito | Resposta curta |
|----------|---------------|
| **Overfitting** (6) | Regularização (zera/encolhe), cross-val, early stopping, dropout, +dados, simplificar |
| **Imbalance** (5) | Class weights, SMOTE, undersampling, mudar métrica (F1/PR-AUC), threshold tuning |
| **Data leakage** | Modelo espia futuro. Prevenir: split temporal, pipeline idêntico treino/serving |
| **Train-serving skew** | Features diferentes treino vs prod. Prevenir: Feature Store compartilhado |
| **Data drift** | Inputs mudam (novas cidades). Detectar: PSI/KL |
| **Concept drift** | Relação input→output muda (home office). Detectar: monitorar métricas |
| **Feedback loops** | Modelo contamina dados. Fix: exploration ε-greedy, boost novos, position debiasing |

```
┌─────────── OFFLINE (batch) ──────────────────────────────────────────────┐
│                                                                          │
│  Data Sources ──→ Kafka/S3 ──→ Spark/Databricks ──→ Feature Store        │
│  (DB, events,      (ingest)     (transform,          (Butterfree:        │
│   APIs, logs)                    clean, agg)           S3 offline +      │
│                                                        Cassandra online) │
│                                       ↓                                  │
│                                  Training Set                            │
│                              (X_train, y_train)                          │
│                                       ↓                                  │
│                                Train Model ──→ Evaluate ──→ MLflow       │
│                                (XGBoost)    (NDCG,F1,RMSE) (registry,   │
│                                                              version)    │
└──────────────────────────────────────────────────────────────────────────┘

┌─────────── ONLINE (real-time) ───────────────────────────────────────────┐
│                                                                          │
│  User Request ──→ API ──→ Retrieval (ES) ──→ Feature Lookup ──→ Model   │
│                           500K → 500          (Cassandra/Redis)  Serving │
│                                                                  (K8s)  │
│                                                    ↓                     │
│                                              Re-rank (rules) ──→ Response│
│                                              (diversidade,       (<200ms)│
│                                               boost novos)               │
└──────────────────────────────────────────────────────────────────────────┘

┌─────────── MONITORING (contínuo) ────────────────────────────────────────┐
│                                                                          │
│  Predictions ──→ Kafka (async logs) ──→ Dashboard ──→ Alertas           │
│  (~8M/dia)                                                               │
│                                                                          │
│  O que monitorar:                                                        │
│  • Model perf (CTR, conversão diária)                                    │
│  • Feature health (% nulls, distribuição)                                │
│  • Data drift (PSI/KL)         ──→ trigger retrain                       │
│  • Latência (P50, P99)         ──→ escalar pods                          │
│                                                                          │
│  Retrain: semanal (scheduled) + triggered (drift/queda)                  │
└──────────────────────────────────────────────────────────────────────────┘
`