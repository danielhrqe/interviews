## Framework ML SD (7 passos)

| # | Passo | Tempo | Fazer |
|---|-------|-------|-------|
| 1 | **Formulation** | 5min | Tipo (ranking/class/reg). Objetivo negócio. Clarifying Qs: logado?, volume?, latência?, métrica hoje? |
| 2 | **Metrics** | 3min | Offline (NDCG/F1/RMSE) + Online (CTR/conversão) + A/B test |
| 3 | **Data & Labels** | 5min | Fontes, label implícito c/ hierarquia, split TEMPORAL |
| 4 | **Features** | 8min | 4 gavetas: Item, User/Session, Context, Cross — 3-4 cada |
| 5 | **Model** | 8min | Baseline heurística → XGBoost → Avançado (LTR/Two-tower) |
| 6 | **Serving** | 5min | Two-stage (Retrieval→Ranking→Re-rank). Online+Offline path. <200ms |
| 7 | **Monitoring** | 5min | Performance, drift, feature health, retrain (semanal + triggered) |

## Métricas — Cola

| Problema | Offline | Online | Cuidado |
|----------|---------|--------|---------|
| **Ranking** | NDCG@10, MRR | CTR, agendamento | NDCG = penaliza bons enterrados |
| **Classificação** | F1, PR-AUC | % detectados, FP rate | NUNCA accuracy c/ imbalance |
| **Regressão** | RMSE, MAE, MAPE | % alugados 30d | RMSE penaliza erros grandes |

| Precision | Recall |
|-----------|--------|
| Alarme falso caro (spam) | Perder positivo caro (fraude) |
| "Dos SIM, quantos eram?" | "Dos reais, quantos pegou?" |

## Problemas QA Resolvidos

| Problema | Tipo | Labels | Modelo | Serving | Detalhe-chave |
|----------|------|--------|--------|---------|---------------|
| **Ranking imóveis (não logado)** ⭐ | Ranking | Implícito: visit>contact>click>view | Popular→XGBoost→LambdaMART | ES 500K→500 → Model → Re-rank | Cold start gradiente. Cross: \|preço-média\| |
| **Preço aluguel** | Regressão | Preço final contrato (não pedido!) | Média×área → XGBoost → Ensemble | Batch ao listar + on-demand | MAPE por bairro. Drift = inflação |
| **RAG contratos** ⭐ | GenAI | N/A | Embedding + LLM | Chunks 512 overlap 50 → pgvector → top-5 → LLM | RAG>FT: dados mudam, mostra fontes. Edge: fora escopo, CPF |
| **Fraude anúncios** | Classif. binária | Moderadores (delayed) | XGBoost + class_weight + threshold=0.3 | Near RT Kafka <5min | RECALL! Imbalance: weights+SMOTE+threshold. Human-in-loop |
| **Recomendação (logado)** | Recomendação | Histórico user | Collab+Content → Two-tower | Offline embeddings → FAISS ANN → re-rank | Dot product user×item. Cold: content-based→collab |

## Conceitos Rápidos

| Conceito | Resposta curta |
|----------|---------------|
| **Overfitting** (6) | Regularização (zera/encolhe), cross-val, early stopping, dropout, +dados, simplificar |
| **Imbalance** (5) | Class weights, SMOTE, undersampling, mudar métrica (F1/PR-AUC), threshold tuning |
| **Data leakage** | Modelo espia futuro. Prevenir: split temporal, pipeline idêntico treino/serving |
| **Train-serving skew** | Features diferentes treino vs prod. Prevenir: Feature Store compartilhado |
| **Data drift** | Inputs mudam (novas cidades). Detectar: PSI/KL |
| **Concept drift** | Relação input→output muda (home office). Detectar: monitorar métricas |
| **Feedback loops** | Modelo contamina dados. Fix: exploration ε-greedy, boost novos, position debiasing |

## Architectures (desenhar no Miro)

```
TWO-STAGE:  500K → [ES/filtros] → 500 → [ML model] → 20 → [Re-rank regras] → Response

ONLINE:  User → API → Ranking Svc → [Redis features + ES candidatos] → Model → Response
OFFLINE: Events → Kafka → Lake → Spark → Feature Store → Train → MLflow → Deploy
```

**Stack QA:** Airflow, Spark/Databricks, Kafka, Feature Store, MLflow, K8s, AWS

## 6 Ajustes Mock

1. Labels **logo no início** (hierarquia implícita)
2. Não falar L1/L2 pelo nome (dizer "zera features" / "encolhe pesos")
3. Cold start = **gradiente** (0→popular, 2-3 clicks→session, muitos→modelo)
4. NDCG = **penaliza bons enterrados**
5. Cross features **com confiança** (|preço-média|, match bairro)
6. Mencionar **feedback loops** (exploration, boost novos)
