# MASTER PREP - Preparação Completa para Entrevistas

> Arquivo único de preparação. Atualizado: 19/fev/2026

---

## Calendário

| # | Empresa | Entrevista | Data | Formato | Ferramenta |
|---|---------|-----------|------|---------|------------|
| 1 | **DoorDash** | System Design (60min) + Team Building (45min) | **26/fev 15h** | Solo, problema hipotético + behavioral | HackerRank whiteboard + Zoom |
| 2 | **Nubank** | Architecture (60min) | **4/mar 10h** | Colaborativo com 2 engenheiros | Draw.io / Miro / Google Drawing |
| 3 | **QuintoAndar** | System Design / ML (60min) | **2/mar 12h** | Conceitos ML/DL/GenAI + case no Figma/Miro | Google Meet |
| 4 | **QuintoAndar** | Coding (60min) | **9/mar 10h** | Algoritmos, 1+ problemas | Codility |
| 5 | **Google** | HR Chat | **23/fev 11h** | Não técnica | - |
| 6 | **Wise** | Pair Programming / Coding (60min) | **27/fev 11h BRT** | Pair programming, Python, OOP-focused | HackerRank CodePair |
| 7 | **Circle** | Resposta | Semana que vem | - | - |

---

# ENTREVISTA 1: DoorDash - 26/fev 13h

## System Design (60 min)

### Formato (do prep kit oficial)
- Problema hipotético (ex: "Design Twitter")
- HackerRank whiteboard (ou outra ferramenta que preferir)
- NÃO é past project — é problema novo

### Critérios de avaliação (oficiais)
| Critério | O que buscam |
|----------|-------------|
| **Structure** | Abordagem sistemática. Articula O QUÊ e POR QUÊ |
| **Comprehensiveness** | Cobre todos os requisitos + edge cases |
| **Feasibility** | Solução prática e implementável |
| **Scalability** | Capacidade de escalar |

### Framework 7 Steps (60 min)

| Step | Tempo | O que fazer |
|------|-------|------------|
| 1. Requirements | 5 min | Functional + non-functional. Pergunte: users, scale, latency, consistency |
| 2. Capacity Estimation | 3 min | QPS, storage, bandwidth (napkin math) |
| 3. API Design | 5 min | Core endpoints. REST verbs, params, responses |
| 4. Data Model | 5 min | Entidades, relacionamentos, DB choice (SQL vs NoSQL) |
| 5. High-Level Architecture | 10 min | Desenhe: LB → App → Cache → DB → Queue |
| 6. Deep Dive | 25 min | Entrevistador escolhe 2-3 componentes. Trade-offs |
| 7. Scaling & Edge Cases | 7 min | Bottlenecks, failure modes, monitoring |

### Problemas DoorDash mais prováveis (ATUALIZADO 23/fev — Hello Interview data com report counts)

**🔴 TIER 1 — MAIS PROVÁVEIS (reportados fev/2026, dezenas de reports):**

**1. Food Item Reviews + Payouts** (37 reports! Mid Feb 2026, Manager level)
- Users rate food items, upvote/downvote reviews, auto payout on threshold
- Sharded hot counters (avoid single-row contention)
- Elasticsearch para search/ranking
- Saga for payouts (idempotent steps + compensation)
- Purchase verification, fraud prevention
- Eventual consistency for vote counts, strong consistency for payouts

**2. Donations Website** (26 reports, Early Feb 2026, Manager level)
- 24-48h charity event, payment processing, failure handling
- Idempotency keys, state machine (initiated→authorized→captured)
- Circuit breaker + failover payment processor
- Redis live counters + WebSocket/SSE for real-time totals
- Backup payment methods when primary fails

**🟡 TIER 2 — PROVÁVEIS (10+ reports, últimos meses):**

**3. Job Scheduler** (11 reports, Late Jan 2026, Manager level)
- 10K jobs/sec, cron + ad-hoc, retry, 1yr history
- Partitioned scheduling, Redis sorted sets, DynamoDB time-bucketed
- Heartbeats/leases, jittered retries, backpressure
- Exactly-once via leasing + idempotency

**4. Review + Rewards** (11 reports, Mid Jan 2026 — variação do #1)
- Reviews + monetary rewards based on quality
- Async scoring pipeline, saga workflows
- Kafka events, denormalization, idempotent payouts with ledger

**5. Instagram / Photo Sharing** (10 reports, Late Nov 2025, Manager level)
- Upload photos, follow users, chronological feed
- Precomputed fan-out feeds, direct-to-S3 upload
- Kafka fan-out, Redis feed cache, DynamoDB metadata

**🔵 TIER 3 — POSSÍVEIS (poucos reports ou antigos):**

**6. Delivery Dispatch System** (clássico, mas 0 reports recentes!)
- Match orders com drivers em real-time
- Geospatial indexing, state machine, Kafka

**7. Metrics Aggregator** (2 reports, Feb 2025 — velho)
- Histogram data, time-bucketed aggregation

### ⚠️ CONCLUSÃO: O que DOMINA no DoorDash SD (dados reais)
1. **Payments/payouts** — tema #1 com 63+ reports combinados
2. **Idempotency + saga** — obrigatório em TODAS as top questions
3. **Redis** — counters, cache, sorted sets, rate limiting
4. **Kafka** — backbone em tudo
5. **State machines** — payment states, job states
6. **Delivery logistics NÃO aparece** — foco mudou para plataformas de conteúdo + pagamentos

### Design Patterns DoorDash
- **Finite State Machine** — order state transitions
- **Event-Driven** — Kafka como backbone
- **Circuit Breaker / Retry** — driver offline → heartbeat → grace → reassign
- **CQRS** — separate read/write paths
- **Geospatial Indexing** — quadtrees, geohashing, S2 cells

### ALERTA: Interrupções
Candidatos reportam entrevistador interrompendo e pulando pra componentes que você ainda não cobriu. Resposta:
1. Acknowledge a pergunta
2. Resposta rápida (2-3 frases)
3. "I'll go deeper on that once I finish the high-level flow"

### Napkin Math Reference

| Metric | Value |
|--------|-------|
| 1 day | ~100K seconds |
| 1M req/day | ~12 QPS |
| 1B req/day | ~12,000 QPS |
| 1 KB × 1M | 1 GB |
| 1 KB × 1B | 1 TB |
| Redis GET | ~0.1 ms |
| DB query (indexed) | 1-10 ms |
| Same-DC RTT | ~0.5 ms |
| Cross-region RTT | ~50-150 ms |

**DoorDash-specific:**
- Active dashers peak: ~1M
- GPS updates: every 5s → 200K updates/sec
- Orders/day: ~10M
- Dispatch latency: <500ms
- Tracking update: <200ms

### Common Components Cheat Sheet

| Componente | Quando usar |
|-----------|-------------|
| **Load Balancer** | Distribuir tráfego (L7 ALB, L4 NLB) |
| **Cache (Redis)** | Reduzir DB load, low latency. Cache-aside, write-through |
| **Message Queue (Kafka)** | Async, decouple services, event streaming |
| **CDN** | Static content, global distribution |
| **Elasticsearch** | Full-text search, fuzzy, geo |
| **S3/Blob** | Files, data lake |
| **PostgreSQL** | ACID, joins, structured data |
| **DynamoDB/Cassandra** | Flexible schema, horizontal scale |
| **WebSocket** | Real-time bidirectional (tracking, chat) |

### CAP Theorem
- **CP**: Financial transactions → PostgreSQL, DynamoDB (strong)
- **AP**: Location updates, feeds → Cassandra, DynamoDB (eventual)

---

## Team Building & Hiring (45 min)

### Formato (do prep kit oficial)
> "Be prepared to talk through who you are as a people leader. Topics: performance management, partnership with recruiting, best practices for team building, growing and mentoring employees."

### Tips oficiais
- Use STAR method
- Have real-life examples and stories ready

### 5 Números para decorar
1. **0 → 21 pessoas** em 3 anos (8-11 diretos)
2. **600+ usuários** na plataforma global
3. **2M queries/day** + 70K daily executions
4. **$2M de economia** em otimização
5. **7+ promoções** patrocinadas + 15+ contratações

### Histórias STAR (arquivo completo: companies/doordash/star-stories.md)

| História | Use para | Resultado-chave |
|----------|----------|----------------|
| H1: Time do zero (0→21) | Team building, hiring, scaling | 600 users, 2M queries/day, $2M savings |
| H2: Migração global (NA merge) | Cross-functional, stakeholder conflict | 2K assets migrated, unified platform |
| H3: Desligamento | Performance management | Changed hiring process, team morale up |
| H4: Promoções (7+) | Coaching, mentoring | SRE → Principal Architect, 25% raise |
| H5: Diversidade | D&I, hiring practices | 4/7 promoções Black/Brown |
| H6: Conflito stakeholders | Influence without authority | RFC process, pair programming with Principal |
| NOVA: 60% do time transferido | Disagree & commit, resilience | Rebuilt team, read the momentum |

### Resposta "Ignore the underperformer"
> "I wouldn't ignore it, for two reasons. First, for the individual — everyone deserves a fair chance with clear expectations and support. Second, for the team — when you don't address underperformance, the whole team notices. It erodes trust, increases workload on top performers, and eventually your best people leave. My job is to act fast — but fair."

### Resposta "Diversity"
> Pipeline diverso (parou de buscar só em faculdades top) + processo estruturado (5 perguntas iguais pra todos) + vagas afirmativas + **resultado: 4 de 7 promoções foram de engenheiros Black/Brown** + inclusão ativa (projetos de alta visibilidade pra todos)

### Resposta "Why DoorDash"
> Scale e complexidade do 3-sided marketplace + cultura de ownership e "1% better every day" + data/ML central ao negócio + desafios de engenharia na escala DoorDash

### Regras para todas as respostas
1. Comece com **2 frases de CONTEXTO** antes da ação
2. Termine com **NÚMERO/RESULTADO** quantificado
3. Use "**I** did" não "we did"
4. Máximo **2-3 minutos** por história

---

# ENTREVISTA 2: Nubank Architecture - 4/mar 10h

## Formato (do prep kit oficial)
- **60 min, colaborativo** com engenheiros Nubank
- Ferramentas: Draw.io/diagrams.net, Miro, Google Jamboard, Google Drawing
- Introdução pessoal: **máximo 5 min**
- Avaliam: como você trabalha em grupo + como desenvolve a solução

## O que esperam de você (oficial)
1. **Justificar escolhas** — saber o porquê de cada ferramenta/técnica
2. **Explicar o raciocínio** — foco no processo, não na resposta perfeita
3. **Solução flexível, sustentável e escalável**
4. **Perguntar!** — não tenha medo de dizer que não sabe algo

## Best practices (oficiais)
- **Co-build**: dê sugestões, opiniões. É colaboração, não apresentação
- **Processo > resultado**: não precisa "terminar" o exercício
- **Whiteboard = comunicação**: não precisa ficar bonito, precisa ser claro
- **Stop and think**: a cada ~10 min, pare e avalie o que foi feito e o que melhorar

## Problemas mais prováveis (de reports de candidatos)

**1. Event Feed System** (MAIS CITADO)
- Design sistema para listar eventos/transações em um feed
- Follow-ups: offline support, sync strategy, ordering, deduplicação
- Por que é Nubank: sistema inteiro é event-driven, feed de transações é core

**2. Chargeback/Dispute System**
- Card brand envia dados via FTP 4x/dia em CSV
- Avaliam: fault tolerance, async processing, idempotency

**3. File Transfer/Integration**
- Mover arquivo entre ambientes cloud e servidor externo
- Retry patterns, exactly-once delivery

**4. Redesign de subsistema Nubank**
- Open-ended: dado a escala (100M+ users, 72B events/day), re-arquitetar subsistema

## Conceitos Nubank que PRECISA saber

### 1. Event-Driven + Kafka (O MAIS IMPORTANTE)
- Nubank processa **72 bilhões de eventos/dia** via Kafka
- Partitioning, consumer groups, exactly-once semantics
- Dead letter queues para fault tolerance
- Circuit breakers: converte exceções em lag (pausa consumers)
- **Idempotência**: correlation IDs para deduplicação

### 2. Imutabilidade como princípio
- Datomic: append-only database ("Git for your data")
- Fatos se tornam true/false, nunca são sobrescritos
- Financial systems precisam de full audit trail

### 3. Hexagonal Architecture (Ports & Adapters)
- Business logic totalmente isolada de infraestrutura
- Ports = interfaces, Adapters = implementações
- Facilita testes e troca de tecnologias

### 4. Simple vs Easy
- **Simple**: menos dependências, mais clareza (preferido!)
- **Easy**: conveniente curto prazo mas complexo longo prazo
- Nubank SEMPRE prefere simple. Esteja preparado pra justificar simplicidade.

### 5. Scalability Units
- NÃO usam sharding de DB
- Clonam infraestrutura inteira por partição de clientes
- Global routing service mapeia clientes para shards

### 6. Financial Patterns
- Double-entry accounting (real-time)
- Compensating transactions (saga pattern)
- Real-Time Gross Settlement para transferências inter-shard

## Diferença DoorDash vs Nubank

| Aspecto | DoorDash | Nubank |
|---------|----------|--------|
| Estilo | Solo, você apresenta | Colaborativo, vocês desenham juntos |
| Foco | Escala e performance | Simplicidade e sustentabilidade |
| Stack | Qualquer | Implicitamente espera Kafka/event-driven |
| Resultado | Resposta correta importa | Processo de discussão importa |
| Comportamento ideal | Liderar o design com confiança | Colaborar, perguntar, co-construir |

---

# ENTREVISTA 3: QuintoAndar ML - ~3-6 mar

## Formato (do prep kit oficial)
- **60 min, sem código**
- Perguntas técnicas diretas: ML, Deep Learning, GenAI
- Case de negócio no Figma ou Miro
- Foco: como você pensa, justifica escolhas, considera escalabilidade e evolução

## Tópicos confirmados
- ML fundamentals (regression, classification, clustering)
- Deep Learning (transformers, embeddings, attention)
- GenAI (RAG, LLMs, agents, prompt engineering)
- MLOps (feature stores, serving, monitoring, drift)
- Bias-variance, overfitting/underfitting
- Model evaluation metrics

## Flashcards de conceitos (self-test)

| # | Pergunta | Resposta |
|---|----------|---------|
| 1 | Gradient descent? | Algoritmo que minimiza erro iterativamente. Learning rate = step size |
| 2 | High learning rate? | Erro oscila, não converge → diminuir LR |
| 3 | Overfitting? | Modelo decorou treino. Train 99%, test 60%. Fix: regularização, menos complexidade |
| 4 | Underfitting? | Modelo não aprendeu. Train 55%, test 50%. Fix: mais complexidade, mais features |
| 5 | Bias-Variance? | High Bias = underfitting. High Variance = overfitting. Goal: balancear |
| 6 | L1 vs L2? | L1 (Lasso): zera features inúteis. L2 (Ridge): shrink all weights |
| 7 | Data Drift vs Concept Drift? | Data: inputs mudaram. Concept: relação mudou. Ambos → retrain |
| 8 | **Precision?** | Dos que acusei, quantos estavam certos? (confiança na acusação) |
| 9 | **Recall?** | Dos que existiam, quantos peguei? (capacidade de captura) |
| 10 | F1 Score? | Média harmônica de Precision e Recall |
| 11 | AUC-ROC? | Capacidade de separar classes. 0.5 = random, 1.0 = perfeito |
| 12 | Supervised vs Unsupervised? | Supervised: tem labels. Unsupervised: descobre padrões |
| 13 | CNN, RNN, Transformer? | CNN: imagens. RNN/LSTM: sequências. Transformer: attention, base dos LLMs |
| 14 | Embeddings? | Texto → vetor numérico. Textos similares ficam próximos |
| 15 | RAG? | LLM + busca em docs reais → reduz alucinação |

## Cases mais prováveis

**Case A - ML Platform Design:**
"Precisamos onboardar 10 data scientists. Como você desenha uma plataforma que vai de ideia a produção em 2 semanas?"
→ Feature store, training pipeline, experiment tracking, CI/CD, serving, monitoring

**Case B - RAG System (aprofundando Tech Screening):**
"Design RAG para chatbot de suporte com 306 categorias."
→ Chunking, embedding model, retrieval, reranking, evaluation, hallucination monitoring

**Case C - Model Monitoring & Drift:**
"Modelo de precificação deployado há 6 meses. Como saber se funciona?"
→ Data drift vs concept drift, testes estatísticos, triggers retraining, A/B testing

**Case D - Feature Store:**
"Feature store para recomendação servindo batch training e real-time inference."
→ Offline (S3) vs online (Cassandra), point-in-time correctness, latência

**Case E - Recommendation System:**
"Design sistema de recomendação de imóveis do QuintoAndar."
→ Collaborative filtering, content-based, ranking, A/B testing, cold start

## ML System Design Framework (7 steps)

| Step | Tempo | O que |
|------|-------|-------|
| 1. Problem Framing | 5 min | Business → ML problem. Classification? Regression? Ranking? |
| 2. Data | 5 min | Que dados existem? Volume? Qualidade? Labeling? |
| 3. Features | 5 min | Feature engineering. Online vs offline. Feature store? |
| 4. Model | 5 min | Baseline → simple → complex. Por que este modelo? |
| 5. Training | 5 min | Pipeline: data → features → train → evaluate → register |
| 6. Serving | 5 min | Batch vs online inference. Latency. A/B testing. Canary |
| 7. Monitoring | 5 min | Model perf + data quality + infra. Drift → retrain trigger |

## RAG Architecture Reference
```
User Query → [Embedding] → Query Vector
    → [Vector DB Search] → Top K chunks
    → [Context Assembly] → Query + Chunks
    → [LLM Inference] → Response
    → [Post-processing] → Final Answer
```

## Stack QuintoAndar (saiba falar sobre)
| Categoria | Ferramentas |
|-----------|-------------|
| ML Platform | QuintoML (monorepo interno) |
| Feature Store | Butterfree (open-source, Spark, S3 offline, Cassandra online) |
| Streaming | Kafka |
| GenAI | LangChain, LangGraph, LlamaIndex, Azure OpenAI |
| Data | Databricks, Unity Catalog |
| Build | Pants (monorepo Python) |

## Seu ângulo forte
Sua experiência construindo plataforma de dados/ML é EXATAMENTE o que o role pede. Frame como: **"Como eu construo isso para escalar para um time de 20 data scientists"**

## Comparison: Your Stack vs QA Stack
| Componente | Sua plataforma | QuintoAndar |
|-----------|---------------|-------------|
| Compute | Databricks/Spark on K8s | Databricks (Spark) |
| Orchestration | Airflow (4K+ DAGs) | Airflow |
| Model Serving | K8s + ArgoCD | K8s-based |
| Experiment Tracking | MLflow | MLflow |
| IaC | Terraform/Terragrunt | Infrastructure as Code |
| CI/CD | GitHub Actions + ArgoCD | CI/CD pipeline |
| Development | Trunk-based, 3-min deploy | Trunk-based |

---

# ENTREVISTA 4: QuintoAndar Coding - ~9-13 mar

## Formato (do prep kit oficial)
- **Codility**, 40 min, 1+ problemas
- Linguagem livre (usar **Python**)
- IDE online com syntax highlight, code completion, e execução
- Avaliam: lógica, clareza, eficiência, boas práticas

## O que estudar (oficial)
1. Programming language + OOP + testing
2. Data structures: arrays, linked lists, stacks, queues, sets, maps, trees, graphs
3. Big-O (time + space complexity)
4. Sorting: insertion sort, quicksort, mergesort
5. Recursion
6. Correctness: use IDE features, run and test

## Pattern Templates (Python)

### HashMap
```python
# Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# Frequency
from collections import Counter
freq = Counter(items)
most_common = freq.most_common(3)

# Group by
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[key(item)].append(item)
```

### Two Pointers
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target: return [left, right]
        elif s < target: left += 1
        else: right -= 1
```

### Sliding Window
```python
# Fixed size: max sum of subarray of size k
def max_sum_k(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best
```

### Binary Search
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1
# O(log n)
```

### BFS Grid
```python
from collections import deque
def bfs_grid(grid, starts):
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()
    for r, c in starts:
        dist[r][c] = 0
        queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1 and grid[nr][nc] != 'X':
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist
```

### Stack
```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]: return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0
```

### Sorting with key=
```python
intervals.sort(key=lambda x: x[0])
items.sort(key=lambda x: (-x[1], x[0]))
most_frequent = max(freq, key=freq.get)
```

### Collections essenciais
```python
from collections import Counter, defaultdict, deque

Counter([1,2,2,3,3,3])        # {3:3, 2:2, 1:1}
defaultdict(list)              # missing key → []
defaultdict(int)               # missing key → 0
deque()                        # O(1) append/pop both ends
# NUNCA use list.pop(0) — é O(n)!
```

## Pattern Recognition
| Sinal no problema | Pattern |
|-------------------|---------|
| Array sorted | Two Pointers / Binary Search |
| Subarray/substring | Sliding Window |
| Frequency/lookup | HashMap |
| Shortest path | BFS |
| Matching/nesting | Stack |

## Python Gotchas
- `def f(x=[])` → mutable default! Use `def f(x=None): x = x or []`
- `/` retorna float; use `//` para int division
- `sort()` = O(n log n)
- Generator: não consuma duas vezes sem resetar

## Pre-Interview Checklist (30 min antes)
- [ ] Codility carregado e testado (fazer demo test oficial!)
- [ ] Python boilerplate: `from collections import Counter, defaultdict, deque`
- [ ] Webcam, mic, screen share testados
- [ ] Água, sala quieta, celular silenciado
- [ ] Lembrete: brute force primeiro, otimiza depois, fale o tempo todo

---

# APÊNDICE: Plano de Estudos Dia-a-Dia

Ver arquivo detalhado: [plano-semana-26fev.md](./plano-semana-26fev.md)

### Resumo
| Período | Foco |
|---------|------|
| 20-25/fev | DoorDash (SD mocks + leadership polish) |
| 26/fev | **DOORDASH 13h** |
| 27/fev - 3/mar | Nubank (event-driven, Kafka, hexagonal) + QA ML (conceitos) |
| 4/mar | **NUBANK 10h** |
| 3-6/mar | **QA ML INTERVIEW** |
| 6-12/mar | QA Coding (Codility, algoritmos, Python) |
| 9-13/mar | **QA CODING** |
