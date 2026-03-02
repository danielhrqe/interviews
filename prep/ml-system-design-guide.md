# ML System Design — Guia Completo para Entrevista

> Preparado para: QuintoAndar TLM MLOps (2/mar) + entrevistas futuras
> Foco: ML Interview (Figma/Miro, SEM código, 1h)

---

## PARTE 1: CONCEITOS FUNDAMENTAIS (Revisão Rápida)

### 1.1 Tipos de Problema ML

| Tipo | Pergunta | Output | Exemplo QuintoAndar |
|------|----------|--------|---------------------|
| **Classificação** | Sim ou não? | Classe (0/1) | "Esse imóvel vai alugar em 30 dias?" |
| **Regressão** | Quanto? | Número contínuo | "Qual o preço justo desse imóvel?" |
| **Ranking** | Em que ordem? | Lista ordenada | "Quais imóveis mostrar primeiro?" |
| **Recomendação** | O que sugerir? | Lista personalizada | "Imóveis que esse usuário vai gostar" |
| **Clustering** | Que grupos existem? | Agrupamentos | "Segmentar tipos de inquilinos" |

**Regra na entrevista:** sempre comece dizendo **que tipo de problema é**. "Isso é um problema de ranking/classificação/regressão."

---

### 1.2 Métricas — Saber de Cor

#### Classificação

| Métrica | Fórmula | Quando usar | Lembrete |
|---------|---------|-------------|----------|
| **Precision** | TP / (TP + FP) | Custo de alarme falso é alto | "Dos que disse SIM, quantos eram SIM?" |
| **Recall** | TP / (TP + FN) | Custo de PERDER positivo é alto | "Dos SIMs reais, quantos pegou?" |
| **F1** | 2 × (P×R)/(P+R) | Equilíbrio entre P e R | Média harmônica |
| **AUC-ROC** | Área sob curva ROC | Comparar modelos, independe de threshold | 0.5 = chute, 1.0 = perfeito |
| **PR-AUC** | Área sob curva Precision-Recall | **Classes desbalanceadas** | Melhor que AUC-ROC com imbalance |

**Quando priorizar qual:**
- **Precision** → spam filter (não quero bloquear email bom)
- **Recall** → detecção de fraude, diagnóstico de câncer (não posso deixar passar)
- **F1** → quando ambos importam igualmente

#### Ranking (SABER EXPLICAR — vai cair!)

| Métrica | O que mede | Intuição |
|---------|-----------|----------|
| **NDCG@K** | Qualidade da lista inteira nos top K | "Os melhores estão no topo?" Penaliza resultados bons enterrados |
| **MAP** | Mean Average Precision | Média das precisions em cada posição relevante |
| **MRR** | Mean Reciprocal Rank | "Quão rápido o user acha o primeiro resultado bom?" |

**Na entrevista, sempre dizer:**
> "Offline uso NDCG@10 pra avaliar a qualidade do ranking. Online uso CTR e taxa de conversão (agendamento de visita) via A/B test."

#### Regressão

| Métrica | Quando usar |
|---------|-------------|
| **RMSE** | Penaliza erros grandes (preço de imóvel) |
| **MAE** | Erros em escala real, robusto a outliers |
| **R²** | "Quanto o modelo explica" (0-1) |

---

### 1.3 Overfitting — 6 Técnicas (de cor!)

Problema: treino 99%, teste 65%. Modelo decorou.

| # | Técnica | Como funciona |
|---|---------|---------------|
| 1 | **Regularização L1/L2** | Penaliza pesos grandes. L1 zera features inúteis, L2 encolhe todos |
| 2 | **Cross-validation (k-fold)** | Treina em K subsets, avalia em cada um. Detecta overfitting |
| 3 | **Early stopping** | Para o treino quando validation loss começa a subir |
| 4 | **Dropout** (deep learning) | Desliga neurônios aleatórios durante treino. Força redundância |
| 5 | **Mais dados** | Mais exemplos = mais difícil decorar |
| 6 | **Simplificar modelo** | Menos layers, menos features, menor max_depth |

---

### 1.4 Class Imbalance — 5 Técnicas (de cor!)

Problema: 95% classe negativa, 5% positiva. Modelo diz "não" pra tudo e acerta 95%.

| # | Técnica | Como |
|---|---------|------|
| 1 | **Class weights** | `class_weight='balanced'` — penaliza mais erros na classe rara |
| 2 | **SMOTE** | Gera exemplos sintéticos da classe minoritária (interpola entre vizinhos) |
| 3 | **Undersampling** | Reduz exemplos da classe majoritária |
| 4 | **Mudar métrica** | Usar F1, PR-AUC, recall — NÃO accuracy |
| 5 | **Threshold tuning** | Modelo dá probabilidade. Cortar em 0.2 em vez de 0.5 |

**Frase pra entrevista:**
> "Com 95/5 split, accuracy é inútil. Uso F1 ou PR-AUC como métrica, class weights no modelo, e ajusto o threshold de decisão baseado no trade-off de negócio."

---

### 1.5 Data Leakage & Train-Serving Skew

#### Data Leakage (vazamento de dados)
O modelo "trapaceia" no treino usando informação que não existiria em produção.

**Exemplos:**
- Usar "data da proposta" pra prever se imóvel vai receber proposta (no treino tem, em produção não)
- Target encoding sem separar treino/teste
- Features calculadas com dados futuros

**Como prevenir:**
- Sempre split temporal (treino = passado, teste = futuro)
- Nunca usar informação pós-evento como feature
- Pipeline de features idêntico entre treino e serving

#### Train-Serving Skew
Features calculadas de forma diferente no treino vs produção.

**Exemplos:**
- Treino usa batch Spark com média dos últimos 30 dias. Serving calcula em real-time com janela diferente
- Normalização com parâmetros diferentes
- Feature store desatualizado

**Como prevenir:**
- **Feature Store** compartilhado entre treino e serving
- Mesmo código de transformação
- Monitorar distribuições das features em produção

---

### 1.6 Drift (Revisão rápida)

| Tipo | O que muda | Exemplo QuintoAndar | Como detectar |
|------|-----------|---------------------|---------------|
| **Data drift** | Distribuição dos inputs | Expansão pra novas cidades, perfil de imóveis muda | PSI, KL divergence nas features |
| **Concept drift** | Relação input→output | Home office: "perto do metrô" perde relevância | Monitorar métricas do modelo ao longo do tempo |

---

### 1.7 RAG — Framework Limpo

**O que é:** Retrieval-Augmented Generation. Dá ao LLM acesso a dados externos pra responder com base em fatos reais.

**3 componentes:**

```
1. INGESTION (offline)
   Documentos → Chunking → Embedding Model → Vector Database

2. RETRIEVAL (online)
   Query do user → Embedding → Similarity Search → Top-K documentos

3. GENERATION (online)
   Prompt + Contexto recuperado → LLM → Resposta fundamentada
```

**RAG vs Fine-tuning:**

| Aspecto | RAG | Fine-tuning |
|---------|-----|-------------|
| Dados atualizados | Atualiza o banco, sem retreinar | Precisa retreinar |
| Custo | Baixo | Alto (GPU, tempo) |
| Alucinação | Menor (tem fonte) | Maior |
| Quando usar | Knowledge base, dados que mudam | Mudar estilo/comportamento do modelo |
| Interpretabilidade | Alta (mostra fontes) | Baixa |

**Chunking strategies (podem perguntar):**
- **Fixed size**: 512 tokens com overlap de 50. Simples, funciona bem
- **Semantic**: quebra por parágrafos/seções. Melhor qualidade, mais complexo
- **Recursive**: tenta quebrar por parágrafo, se muito grande quebra por sentença

---

### 1.8 Modelos — Quando Usar Qual

| Modelo | Tipo de dado | Quando usar | Trade-off |
|--------|-------------|-------------|-----------|
| **Logistic Regression** | Tabular | Baseline, interpretável | Rápido mas limitado |
| **Random Forest** | Tabular | Bom default, robusto | Lento em produção com muitas árvores |
| **XGBoost/LightGBM** | Tabular | **Melhor pra dados tabulares** | Estado da arte, rápido, interpretável |
| **Neural Network** | Texto, imagem, sequência | Dados não-estruturados | Precisa de muitos dados, caixa preta |
| **Transformer** | Texto, multimodal | NLP, embeddings | Pesado, caro |

**Regra de ouro na entrevista:**
> "Começo com um baseline simples (logistic regression ou heurística), depois itero pra XGBoost. Só vou pra deep learning se os dados justificarem (texto, imagem, sequência)."

---

## PARTE 2: FRAMEWORK ML SYSTEM DESIGN (7 passos)

Esse é o framework pra usar na entrevista de segunda-feira. Cada passo com tempo sugerido.

### Passo 1: Problem Formulation (5 min)

**O que fazer:**
1. Repetir o problema nas suas palavras
2. Perguntar requisitos (clarifying questions)
3. Definir: que tipo de problema ML é? (ranking, classificação, etc.)
4. Definir: qual o objetivo de negócio?

**Perguntas pra fazer ao entrevistador:**
- "O usuário está logado ou não? Tenho histórico?"
- "Qual o volume de dados? Quantos itens pra rankear?"
- "Latência importa? É real-time ou batch?"
- "Como é medido sucesso hoje? Qual métrica de negócio?"

**Template de resposta:**
> "Esse é um problema de [RANKING/CLASSIFICAÇÃO/REGRESSÃO]. O objetivo de negócio é [MÉTRICA]. Vou começar definindo as métricas, depois features, modelo, e por fim serving e monitoramento."

---

### Passo 2: Metrics (3 min)

**Sempre definir DUAS camadas:**

| Camada | Métricas | Por quê |
|--------|----------|---------|
| **Offline** | NDCG@K, F1, AUC, RMSE | Avaliar modelo antes de deploy |
| **Online** | CTR, conversão, revenue, tempo de sessão | Impacto real no negócio |

**Dizer:**
> "Offline uso [MÉTRICA] pra iterar rápido no modelo. Online uso [MÉTRICA DE NEGÓCIO] via A/B test pra validar impacto real."

**Cuidado:** um modelo pode ter bom NDCG offline mas não converter online. Por isso A/B test é obrigatório.

---

### Passo 3: Data & Labels (5 min)

**3 perguntas a responder:**

1. **De onde vêm os dados?**
   - Banco de dados (imóveis, users)
   - Event logs (clicks, views, agendamentos)
   - APIs externas (geolocalização, transporte)

2. **Qual é o label (target)?**
   - Explícito: user deu rating, marcou favorito
   - Implícito: click, tempo na página, agendou visita, fechou contrato
   - **Hierarquia de sinais**: contrato > visita > contato > click > view

3. **Como construo o training set?**
   - Cada row = (query, item, label)
   - Split temporal: treino no passado, teste no futuro (NUNCA random split pra dados com tempo!)

**Armadilhas comuns (vão testar isso):**
- Label delay: user viu imóvel hoje, assinou contrato em 30 dias. Quando considero positivo?
- Selection bias: só tenho dados de itens que foram mostrados (modelo antigo enviesou os dados)
- Label sparsity: 99% dos pares (user, item) não tem interação

---

### Passo 4: Feature Engineering (8 min) ← MAIS IMPORTANTE

**Categorizar features em 4 grupos:**

#### a) Item Features (do imóvel)
- Preço, preço/m², quartos, área
- Bairro, cidade, distância do metrô
- Qualidade das fotos (score de CNN)
- Dias publicado, quantidade de views/clicks históricos
- Taxa histórica de aluguel (imóveis similares no bairro)

#### b) User Features (do usuário)
- Se logado: histórico de buscas, favoritos, faixa de preço preferida
- Se NÃO logado: sessão atual (clicks, tempo na página, filtros usados)
- Device (mobile/desktop), localização IP

#### c) Context Features (do momento)
- Hora do dia, dia da semana
- Sazonalidade (jan = mudanças, dez = baixa)
- Device type

#### d) Cross Features (user × item)
- Similaridade entre imóvel e histórico do user
- Match entre faixa de preço buscada e preço do imóvel
- Distância entre localização do user e do imóvel

**Na entrevista, LISTAR pelo menos 3-4 de cada categoria.**

---

### Passo 5: Model Selection (8 min)

**Sempre apresentar em 3 estágios: Baseline → V1 → V2**

#### Baseline (heurística, sem ML)
- Ordenar por popularidade (CTR histórico)
- Ordenar por recência (mais recentes primeiro)
- Regras de negócio (imóveis pagos primeiro)

> "O baseline me dá um piso pra comparar. Se o ML não bater o baseline, não vale a complexidade."

#### V1 — Modelo simples
- **XGBoost/LightGBM** com features tabulares
- Pointwise: prever score pra cada item, ordenar por score
- Rápido de treinar, interpretar e servir
- Feature importance mostra o que está funcionando

#### V2 — Modelo avançado (se perguntarem)
- **Learning to Rank (LTR)**: LambdaMART, LambdaRank
  - Pairwise: "imóvel A é melhor que B pra esse user?"
  - Listwise: otimiza NDCG diretamente
- **Two-tower model**: encoder de user + encoder de item, dot product
- **Deep model**: Wide & Deep (Google), DeepFM

**Frase chave:**
> "Começo com XGBoost pointwise porque é rápido, interpretável e serve como baseline forte. Depois itero pra LambdaMART se precisar otimizar NDCG diretamente."

#### Two-Stage Architecture (SABER EXPLICAR!)

```
500K imóveis
    ↓
[RETRIEVAL] — filtros + Elasticsearch → 500 candidatos
    ↓
[RANKING] — modelo ML (XGBoost/LTR) → top 20 ordenados
    ↓
[RE-RANKING] — regras de negócio (diversidade, ads) → resultado final
```

Por que two-stage?
- Não dá pra rodar modelo complexo em 500K itens em <200ms
- Retrieval é rápido (filtros/inverted index), reduz candidatos
- Ranking é preciso (ML), aplica nos candidatos filtrados

---

### Passo 6: Serving & Infrastructure (5 min)

**Manter simples. 2 minutos no máximo.**

```
Online Path:
  User → API → Ranking Service → [Redis features] + [ES candidatos] → Model Serving → Response

Offline Path:
  Event logs → Kafka → Data Lake → Spark (features) → Training → Model Registry → Deploy
```

**Componentes chave (nomear sem detalhar):**
- **Feature Store** (Redis online / Spark offline): mesmas features treino e serving
- **Model Registry** (MLflow): versionar modelos
- **A/B test framework**: comparar modelo novo vs atual

**Latência:**
- Retrieval (ES): ~20ms
- Feature lookup (Redis): ~5ms
- Model inference: ~10-50ms
- Total: <200ms ✅

---

### Passo 7: Monitoring & Iteration (5 min)

**4 coisas pra monitorar:**

| O que | Como | Ação |
|-------|------|------|
| **Model performance** | CTR, conversão diária | Alerta se cair >X% |
| **Data drift** | PSI/KL nas features | Retreinar se drift detectado |
| **Feature health** | % nulls, distribuição | Alerta se feature quebrar |
| **Latência** | P50, P99 do serving | Escalar se subir |

**Retraining strategy:**
- Scheduled: retreinar semanalmente com dados novos
- Triggered: retreinar quando drift detectado ou métricas caem

**A/B testing:**
> "Nunca faço deploy direto. Sempre A/B test com 5% do tráfego, monitoro por 1-2 semanas, depois ramp up gradual."

**Cold Start (vão perguntar!):**
- User novo / não logado: fallback pra **popularidade** (CTR histórico do imóvel)
- Item novo: usar **content-based features** (preço, bairro, fotos) até ter dados de interação
- Conforme sessão avança, ir misturando sinais de sessão com popularidade

---

## PARTE 3: PROBLEMAS RESOLVIDOS

### Problema 1: Ranking de Imóveis para Usuário Não Logado
> (Pergunta mais reportada no QuintoAndar!)

**1. Problem Formulation**
- Problema de **ranking**
- Objetivo: ordenar imóveis de forma relevante sem histórico do usuário
- Constraint: latência <200ms, ~500K imóveis, ~2M buscas/dia (~23 QPS)

**2. Métricas**
- Offline: NDCG@10, MRR
- Online: CTR, taxa de agendamento de visita, tempo na sessão

**3. Data & Labels**
- Dados: listagem de imóveis + event logs (views, clicks, contatos, visitas)
- Label implícito com hierarquia: visita (3) > contato (2) > click (1) > view (0)
- Training set: (query_filters, imóvel, relevance_score)
- Split temporal: últimos 3 meses treino, última semana teste

**4. Features**

| Categoria | Features |
|-----------|----------|
| **Query** | bairro buscado, nº quartos, faixa de preço, tipo (apto/casa) |
| **Item** | preço, preço/m², quartos, área, dias publicado, nº fotos, qualidade fotos, CTR histórico, taxa de aluguel do bairro |
| **Session** | clicks na sessão, últimos imóveis vistos, tempo médio por listing, device |
| **Context** | hora do dia, dia da semana, sazonalidade |
| **Cross** | |preço - preço_médio_buscado|, match bairro query×item |

**5. Modelo**
- Baseline: ordenar por CTR histórico do imóvel (popularidade)
- V1: XGBoost pointwise → prever relevance_score, ordenar
- V2: LambdaMART → otimizar NDCG diretamente

**6. Serving**
```
Query (filtros) → Elasticsearch (retrieval, ~500 candidatos)
                → Feature lookup (Redis: session features, item features)
                → XGBoost inference (~10ms)
                → Re-ranking (diversidade de bairros, boost imóveis novos)
                → Top 20 resultados
```

**7. Cold Start**
- Primeiro acesso, zero sessão: ranking por popularidade (CTR global)
- Após 2-3 clicks na sessão: começa a usar session features
- Após completar busca: ajusta ranking com base nos filtros escolhidos

**8. Monitoramento**
- Daily: NDCG offline, CTR online
- Drift: PSI nas features principais semanalmente
- Alertas: CTR cai >10% em 24h → investigar

---

### Problema 2: Prever Preço de Aluguel de Imóvel

**1. Problem Formulation**
- Problema de **regressão**
- Objetivo: estimar preço justo de aluguel para donos de imóveis
- Impacto: preço alto demais → não aluga. Preço baixo → dono perde dinheiro

**2. Métricas**
- Offline: RMSE, MAE, MAPE (Mean Absolute Percentage Error)
- Online: % de imóveis que alugam em 30 dias com preço sugerido vs sem

**3. Data & Labels**
- Dados: imóveis listados com preço pedido + preço final de contrato
- Label: preço final do contrato (real, não o pedido)
- Split temporal

**4. Features**

| Categoria | Features |
|-----------|----------|
| **Imóvel** | quartos, área, andar, vagas, condomínio, tem mobília |
| **Localização** | bairro, distância metrô, distância centro, nota do bairro (segurança, lazer) |
| **Mercado** | preço médio do m² no bairro (últimos 3 meses), taxa de ocupação, oferta/demanda |
| **Sazonalidade** | mês do ano, tendência de preço (subindo/descendo) |
| **Qualidade** | nº de fotos, score de qualidade das fotos, tamanho da descrição |

**5. Modelo**
- Baseline: média de preço/m² do bairro × área
- V1: XGBoost regressor
- V2: Ensemble (XGBoost + LightGBM + Ridge) → stacking

**6. Serving**
- Batch: calcular preço sugerido quando imóvel é listado
- On-demand: recalcular quando dono pede reavaliação
- Feature store com dados de mercado atualizados diariamente

**7. Monitoramento**
- MAPE por bairro (detectar regiões onde modelo erra mais)
- Drift: preços do mercado mudam (inflação, crise) → retreinar mensalmente

---

### Problema 3: Sistema RAG para Contratos de Aluguel

**1. Problem Formulation**
- Objetivo: inquilinos e proprietários fazem perguntas sobre contratos e o sistema responde baseado nos documentos reais
- "Posso ter pet?", "Qual a multa por rescisão?", "Quando posso pedir revisão?"

**2. Arquitetura**

```
INGESTION (offline):
  Contratos PDF → Parser → Chunking (512 tokens, overlap 50)
                        → Embedding model (e.g. text-embedding-3-small)
                        → Vector DB (pgvector / Pinecone)

RETRIEVAL + GENERATION (online):
  Pergunta do user → Embedding → Similarity search (top-5 chunks)
                   → Prompt template + chunks → LLM → Resposta
                   → Guardrails (não dar conselho jurídico)
```

**3. Decisões de Design**

| Decisão | Escolha | Por quê |
|---------|---------|---------|
| Chunk size | 512 tokens, overlap 50 | Balanceia contexto vs precisão |
| Embedding model | text-embedding-3-small | Barato, boa qualidade, multilingual |
| Vector DB | pgvector | Já usam Postgres, menos infra |
| LLM | GPT-4 / Claude | Melhor qualidade de resposta |
| Top-K | 5 chunks | Suficiente sem encher contexto |

**4. Métricas**
- Offline: Retrieval accuracy (o chunk correto está no top-5?)
- Online: % de perguntas respondidas sem escalar pra humano, satisfação do user
- Qualidade: human evaluation de respostas (amostra semanal)

**5. Edge Cases**
- Pergunta fora do escopo: "Qual o preço do Bitcoin?" → filtrar com classifier antes
- Informação contraditória entre contratos: retornar ambas + disclaimer
- Dados sensíveis: nunca retornar CPF, dados bancários

---

### Problema 4: Detecção de Anúncios Fraudulentos

**1. Problem Formulation**
- Problema de **classificação binária** (fraude / não fraude)
- Alta consequência: fraude que passa = usuário lesado, dano à marca
- **Priorizar RECALL** (pegar o máximo de fraudes, mesmo com mais falsos positivos)

**2. Métricas**
- Offline: Recall, PR-AUC (NOT accuracy — classes desbalanceadas!)
- Online: % de fraudes detectadas, tempo até detecção, taxa de falso positivo

**3. Data & Labels**
- Label: anúncios marcados como fraude por moderadores (delayed label)
- Problema: ~1% de fraudes (class imbalance severo)
- Solução: SMOTE + class weights + threshold tuning

**4. Features**

| Categoria | Features |
|-----------|----------|
| **Anúncio** | preço vs média do bairro, fotos (reverse image search score), tamanho descrição |
| **Anunciante** | conta nova?, nº de anúncios, verificação de documentos, histórico |
| **Comportamento** | velocidade de criação, horário de postagem, padrão de texto (copy-paste) |
| **Imagem** | duplicada em outros sites?, qualidade, metadados EXIF |

**5. Modelo**
- V1: XGBoost com class_weight + threshold=0.3 (recall alto)
- V2: Ensemble + regras de negócio (preço <50% da média = flag automático)
- Human-in-the-loop: modelo flaga, moderador decide

**6. Serving**
- Near real-time: anúncio criado → evento Kafka → scoring → flag ou aprovar
- SLA: <5 min entre criação e decisão

---

### Problema 5: Recomendação de Imóveis para Usuário Logado

**1. Problem Formulation**
- Problema de **recomendação personalizada**
- Diferença do ranking: aqui TENHO histórico do usuário
- "Imóveis que você pode gostar" na home page

**2. Abordagens**

| Abordagem | Como | Quando |
|-----------|------|--------|
| **Collaborative filtering** | "Users parecidos gostaram de X" | Bastante dados de interação |
| **Content-based** | "Imóveis parecidos com os que você viu" | Poucos dados de interação |
| **Hybrid** | Combina ambos | Produção real |

**3. Two-Tower Model (estado da arte)**

```
User Tower:                    Item Tower:
  user_id                        item_id
  histórico de clicks            preço, quartos, bairro
  buscas recentes                fotos (embedding CNN)
  faixa de preço                 descrição (embedding BERT)
       ↓                              ↓
  User Embedding (128d)         Item Embedding (128d)
       ↓                              ↓
       └──────── Dot Product ─────────┘
                     ↓
               Relevance Score
```

**4. Serving**
- Offline: pre-compute embeddings de todos os itens
- Online: compute user embedding → ANN search (FAISS/ScaNN) → top-K → re-rank

**5. Cold Start**
- User novo: content-based com filtros iniciais + popularidade
- Conforme interage: transition pra collaborative + two-tower

---

## PARTE 4: CHEATSHEET DE ENTREVISTA

### Frases prontas pra usar

**Ao começar:**
> "Antes de mergulhar na solução, quero entender melhor o problema. Posso fazer algumas perguntas?"

**Ao definir métricas:**
> "Vou usar [OFFLINE] pra iterar rápido e [ONLINE] via A/B test pra validar impacto real no negócio."

**Ao escolher modelo:**
> "Começo com um baseline simples pra estabelecer um piso. Depois itero pra [MODELO] porque [RAZÃO]."

**Ao discutir trade-offs:**
> "O trade-off aqui é entre [X] e [Y]. Pra esse caso, priorizo [X] porque [RAZÃO DE NEGÓCIO]."

**Ao falar de cold start:**
> "Pra cold start, uso um fallback baseado em popularidade e content-based features. Conforme coleto sinais de interação, faço transição gradual pro modelo personalizado."

**Ao falar de monitoramento:**
> "Monitoro 3 coisas: performance do modelo, health das features, e drift nos dados. Retreino [FREQUÊNCIA] ou quando métricas caem além do threshold."

### Template de Wrap-up (últimos 2 min)

> "Resumindo: é um problema de [TIPO]. Uso [MODELO] com [N] features principais. Offline avalio com [MÉTRICA], online com [MÉTRICA] via A/B test. Os trade-offs principais são [1] e [2]. Próximos passos seriam [MELHORIA]."

### Red Flags — O que NÃO fazer

- ❌ Pular direto pra arquitetura de infra (Kafka, Redis, API Gateway)
- ❌ Não definir métricas
- ❌ Não mencionar baseline
- ❌ Accuracy como métrica com classes desbalanceadas
- ❌ Não falar de cold start
- ❌ Não falar de monitoramento
- ❌ Random split em dados temporais (sempre split temporal!)
- ❌ Não categorizar features (listar sem estrutura)
