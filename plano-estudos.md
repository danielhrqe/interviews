# Plano de Estudos — Semana 27/fev - 5/mar 2026

> **4 entrevistas em 4 dias consecutivos.**
> DoorDash FEITO (26/fev). Lição: preparar TODOS os problemas, defender decisões com dados.
> Atualizado: 26/fev/2026

---

## Agenda da Semana

| Dia | Entrevista | Horário | Formato |
|-----|-----------|---------|---------|
| Sex 27/fev | — | — | Descanso + início prep QA ML |
| Sáb 28/fev | — | — | Prep intensiva: QA ML + Wise coding |
| Dom 1/mar | — | — | QA ML final + Nubank início |
| **Seg 2/mar** | **QuintoAndar ML** | **12:00-13:00** | Figma/Miro, ML/DL/GenAI + business case, SEM código |
| **Ter 3/mar** | **Wise Pair Programming** | **08:30-09:30** | HackerRank CodePair, Python, colaborativo |
| **Qua 4/mar** | **Nubank Architecture** | **10:00-11:00** | Miro, 2 engenheiros, colaborativo |
| **Qui 5/mar** | **Circle bate-papo** | TBD | Conversa informal 45min, zero prep |

---

# ENTREVISTA 1: QuintoAndar ML (Seg 2/mar 12h)

## Formato
- 1h, Google Meet + Figma/Miro
- Perguntas técnicas diretas: ML, Deep Learning, GenAI
- Business case (SEM código)
- Colaborativo — perguntar e discutir
- **Desabilitar ferramentas de IA** antes da call

## O que avaliam
1. **Decomposição** — quebrar problema em partes menores
2. **Trade-offs** — justificar escolhas com prós/contras
3. **Napkin math** — dimensionar componentes
4. **Design iterativo** — começar simples, melhorar
5. **Fundamentos** — ML, DL, GenAI, MLOps

## Pergunta mais reportada (Glassdoor)
> "Como você construiria um sistema para rankear imóveis para um usuário desconhecido (não logado)?"

## ML Flashcards (self-test, sem consulta)

| # | Pergunta | Resposta |
|---|----------|---------|
| 1 | Supervised vs Unsupervised? | Supervised: tem labels (classificação, regressão). Unsupervised: descobre padrões (clustering) |
| 2 | Overfitting? | Modelo decorou treino. Train 99%, test 60%. Fix: regularização, dropout, mais dados, early stopping |
| 3 | Underfitting? | Modelo não aprendeu. Train 55%, test 50%. Fix: mais complexidade, mais features, menos regularização |
| 4 | Bias-Variance? | High Bias = underfitting. High Variance = overfitting. Goal: balancear |
| 5 | L1 vs L2? | L1 (Lasso): zera features inúteis. L2 (Ridge): shrink all weights |
| 6 | Precision? | Dos que acusei, quantos estavam certos? TP/(TP+FP) |
| 7 | Recall? | Dos que existiam, quantos peguei? TP/(TP+FN) |
| 8 | F1 Score? | Média harmônica Precision × Recall. Usa quando classes desbalanceadas |
| 9 | AUC-ROC? | Capacidade separar classes. 0.5=random, 1.0=perfeito |
| 10 | Cross-validation? | K-fold: divide dados em K partes, treina K vezes rotacionando test set |
| 11 | Gradient descent? | Minimiza erro iterativamente. LR alto: oscila. LR baixo: lento |
| 12 | Data Drift vs Concept Drift? | Data: distribuição dos inputs mudou. Concept: relação input→output mudou |
| 13 | Embeddings? | Texto/items → vetor numérico. Similares ficam próximos no espaço |
| 14 | Transformer/Attention? | Self-attention: cada token "olha" todos os outros. Base dos LLMs |
| 15 | RAG? | LLM + busca em docs reais → reduz alucinação. Chunks → embed → retrieve → generate |
| 16 | Fine-tuning vs RAG? | Fine-tuning: adapta modelo (caro, precisa dados). RAG: adiciona contexto externo (mais barato, atualizado) |
| 17 | Ensemble? | Combina vários modelos. Random Forest (bagging), XGBoost (boosting) |
| 18 | Feature Store? | Repositório centralizado de features. Offline (batch, S3) + Online (low-latency, Redis/Cassandra) |
| 19 | A/B Testing ML? | Modelo novo vs baseline. Métricas: conversão, latência, business metric. Significance test |
| 20 | Cold Start? | Usuário/item novo sem histórico. Fix: popularity, content-based, context features |

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

## Business Case: Ranking de Imóveis (provável)

**Cold start (usuário não logado):**
- Popularity-based: imóveis mais vistos/contactados na região
- Location-based: lat/long do request, raio
- Context features: hora do dia, device, cidade
- Trending: recém-publicados com boa performance

**Features do imóvel:**
- Preço, localização, tipo (apt/casa), quartos, área, fotos (quantidade/qualidade)
- Recência da publicação, popularidade (views, contacts), reviews
- Amenities (piscina, garagem, pet-friendly)

**Modelo:**
- Baseline: sort by popularity × recência
- V1: Gradient Boosting (XGBoost) com features tabulares
- V2: Embedding do imóvel + user embedding (collaborative filtering)
- V3: Two-tower model (user tower + item tower → dot product)

**Métricas:** CTR, conversion (contato→visita→contrato), time-to-rent, NDCG

**Pipeline:** Collect data → Feature eng → Train → A/B test → Deploy → Monitor drift

## RAG Architecture (já caiu no tech screening!)

```
User Query → [Embedding Model] → Query Vector
  → [Vector DB Search] → Top K chunks
  → [Reranking] → Best chunks
  → [Context Assembly] → Query + Chunks + System Prompt
  → [LLM Inference] → Response
  → [Guardrails] → Final Answer
```

**Componentes:** Chunking (overlap), Embedding model (ada-002/e5), Vector DB (pgvector/Pinecone), Reranker, LLM, Evaluation (faithfulness, relevance)

## MLOps — Pipeline End-to-End

```
Data Sources → Feature Store → Training Pipeline → Model Registry
  → Serving (batch/real-time) → Monitoring → Retrain Trigger
```

**Monitoring:** data drift (PSI, KS test), concept drift (model metrics decay), infra (latency, errors)
**CI/CD ML:** data validation → train → evaluate → register → canary deploy → full rollout

## Stack QuintoAndar (mencionar naturalmente)
- Airflow (orquestração), Spark/Databricks (processamento), Kafka (streaming)
- Feature Store próprio (Butterfree, open-source), MLflow, Kubeflow, AWS
- ~8M registros/dia de monitoramento de modelos
- Python (ML), Java/Kotlin (backend)
- GenAI: LangChain, LangGraph, Azure OpenAI

## Comparação: Sua Stack vs QA Stack
| Componente | Sua plataforma | QuintoAndar |
|-----------|---------------|-------------|
| Compute | Databricks/Spark on K8s | Databricks (Spark) |
| Orchestration | Airflow (4K+ DAGs) | Airflow (Cloud Composer) |
| Model Serving | K8s + ArgoCD | K8s-based |
| Experiment Tracking | MLflow | MLflow |
| IaC | Terraform/Terragrunt | Infrastructure as Code |

**Seu ângulo forte:** construiu plataforma de ML do zero para 600+ usuários. Frame: "How I build this to scale for 20+ data scientists"

## Perguntas para fazer ao entrevistador
1. "How does the ML Platform team collaborate with Data Scientists on model deployment?"
2. "What's the biggest challenge in scaling ML monitoring right now?"
3. "How do you handle the cold start problem for new property listings?"

---

# ENTREVISTA 2: Wise Pair Programming (Ter 3/mar 08:30)

## Formato
- 1h, HackerRank CodePair, Python (confirmar com recruiter!)
- Pair programming colaborativo com 1 engenheiro
- NÃO é LeetCode — problemas práticos/domain-relevant
- Requirements podem MUDAR no meio do problema
- **Velocidade importa** (candidato rejeitado por lentidão)
- 11% pass rate em London — altamente seletivo

## O que avaliam (4 dimensões)
1. **Colaboração & Comunicação** — pensar em voz alta, perguntar, discutir
2. **Arquitetura** — organização de código, decisões de design, trade-offs
3. **Problem Solving** — abordagem estruturada, adaptabilidade
4. **Code Quality** — SOLID, DRY, KISS, nomes claros, testabilidade

## Problemas confirmados (Glassdoor/Blind/JoinTaro)

| Problema | Dificuldade | O que testa |
|----------|-------------|-------------|
| **Circuit Breaker** | Medium | OOP, state machine, time-based logic |
| **Currency Converter** | Easy-Medium | Clean code, edge cases, domain Wise |
| **Rate Limiter** | Medium | HashMap, concurrency, time |
| **Sorting Intervals** | Medium | Arrays, sorting, merge |
| **Code Refactoring** | Medium | Recebe código existente → melhora |
| **Integer to Roman** | Easy-Medium | Implementação limpa |

## Estratégia na entrevista
1. Ler problema → perguntar clarificações ANTES de codar
2. Explicar abordagem em 1-2 frases antes de implementar
3. Começar simples → funcionar → refatorar
4. **Pensar em voz alta O TEMPO TODO**
5. Quando requirements mudam: "OK, let me think about how this changes things..."
6. Edge cases: empty input, single element, duplicates

## SOLID Principles (decorar)
- **S**ingle Responsibility — cada classe faz UMA coisa
- **O**pen/Closed — aberto para extensão, fechado para modificação
- **L**iskov Substitution — subclasse substitui pai sem quebrar
- **I**nterface Segregation — interfaces pequenas e específicas
- **D**ependency Inversion — dependa de abstrações, não implementações

## Circuit Breaker — Template Mental

```
States: CLOSED → OPEN → HALF_OPEN → CLOSED

CLOSED: requests passam. Conta falhas. Se falhas >= threshold em window → OPEN
OPEN: requests bloqueados. Após timeout → HALF_OPEN
HALF_OPEN: permite 1 request. Se sucesso → CLOSED. Se falha → OPEN

Config: failure_threshold=3, window=10min, recovery_timeout=5min
```

## Rate Limiter — Template Mental

```
Token Bucket: bucket com N tokens. Cada request consome 1.
  Refill: adiciona tokens a cada intervalo.
  Se bucket vazio → reject.

Sliding Window: HashMap[user_id] → list of timestamps.
  Remove timestamps fora da window. Count < limit → allow.
```

## Merge Intervals — Template Mental

```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

## Collections Python (ter na cabeça)

```python
from collections import Counter, defaultdict, deque

Counter([1,2,2,3,3,3])     # {3:3, 2:2, 1:1}
defaultdict(list)           # missing key → []
defaultdict(int)            # missing key → 0
deque()                     # O(1) append/pop both ends
# NUNCA use list.pop(0) — é O(n)!
```

## Perguntas para fazer ao entrevistador
1. "How do engineers at Wise balance product work with technical debt?"
2. "What does ownership look like in practice for a Staff Engineer?"
3. "What's the most interesting technical challenge your team faced recently?"

---

# ENTREVISTA 3: Nubank Architecture (Qua 4/mar 10h)

## Formato
- 1h, Miro (ou Draw.io/Google Drawings)
- 2 engenheiros Nubank — MUITO colaborativo
- Problema hipotético → desenhar arquitetura juntos
- NÃO precisa "terminar" — processo > resultado
- Introdução pessoal: MAX 5 minutos

## O que avaliam
1. **Colaboração** — como trabalha em grupo, dá sugestões, aceita feedback
2. **Trade-offs** — complexidade vs performance vs custo vs simplicidade
3. **Comunicação** — explicar raciocínio de cada decisão
4. **Flexibilidade** — solução sustentável e escalável
5. **Perguntas** — eles QUEREM que você pergunte

## Dicas do PDF oficial Nubank
- **Não tenha medo de dizer que não sabe**
- Traga sugestões e opiniões sobre a solução
- É colaboração, não apresentação
- Whiteboard = facilitador de comunicação, não precisa ser bonito
- **Pare a cada ~10 min** para avaliar o que foi feito e o que melhorar
- Foco no processo de construção da solução

## Problemas confirmados (Glassdoor)

| Problema | Detalhes | Probabilidade |
|----------|----------|---------------|
| **Event Feed** | Feed de eventos/transações, persistência offline, sync, ordering, deduplicação | MAIS COMUM |
| **Chargeback System** | Integração com bandeira via FTP, processamento batch 4x/dia, CSV, reconciliação | Comum |
| **Redesign Architecture** | "Como redesenharia a arquitetura do Nubank?" — open-ended | Possível |

## Padrões Nubank (USAR na entrevista)

| # | Padrão | O que é | Quando usar |
|---|--------|---------|-------------|
| 1 | **Event Sourcing** | Armazena eventos, não estado. Rebuild state do log | Financial audit trail, undo/replay |
| 2 | **Idempotência** | Correlation IDs, exactly-once processing | Qualquer write operation |
| 3 | **DLQ** | Dead Letter Queue: eventos falhados vão para retry com metadata | Fault tolerance |
| 4 | **Circuit Breaker** | Pausa consumo quando serviço externo falha, acumula lag | Integração externa |
| 5 | **Hexagonal Architecture** | Ports (interfaces) & Adapters (implementações). Core isolado | Toda a codebase Nubank |
| 6 | **Imutabilidade** | Datomic append-only. Fatos nunca sobrescritos | Financial data, audit |
| 7 | **Compensating Transactions** | Saga: se step falha → compensation desfaz steps anteriores | Cross-shard operations |

## Stack Nubank (mencionar naturalmente)

| Tech | Uso |
|------|-----|
| **Clojure** | 1000+ microserviços |
| **Kafka** | Sistema nervoso central, event streaming |
| **Datomic** | Banco imutável append-only ("Git para dados") |
| **AWS** | S3, DynamoDB, EKS |
| **Spark/Scala** | Data processing |
| Hexagonal Arch | Ports & Adapters em tudo |

## Números de escala (napkin math)
- 70M+ usuários
- 1B eventos/dia → ~12K QPS
- 100 TB de eventos processados/dia
- 1000+ microserviços Clojure
- 5M requests internos/minuto
- 450M eventos/dia na plataforma de fraude

## Diferença DoorDash vs Nubank

| Aspecto | DoorDash | Nubank |
|---------|----------|--------|
| Estilo | Solo, você lidera | Colaborativo, vocês desenham juntos |
| Foco | Escala e performance | **Simplicidade** e sustentabilidade |
| Comportamento | Liderar com confiança | **Colaborar, perguntar, co-construir** |
| Resultado | Resposta correta importa | **Processo** de discussão importa |

## Perguntas para fazer ao entrevistador
1. "How do you handle schema evolution in an event-sourced system?"
2. "What's the biggest operational challenge with 1000+ microservices?"
3. "How does the hexagonal architecture work in practice at Nubank's scale?"

---

# CODING PATTERNS — Quick Reference (Wise + QA Codility)

## Pattern Templates Python

### HashMap
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
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

### BFS Grid
```python
from collections import deque
def bfs_grid(grid, starts):
    rows, cols = len(grid), len(grid[0])
    visited = set(starts)
    queue = deque(starts)
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
```

### Sorting
```python
intervals.sort(key=lambda x: x[0])
items.sort(key=lambda x: (-x[1], x[0]))  # desc by [1], asc by [0]
most_frequent = max(freq, key=freq.get)
```

## Pattern Recognition

| Sinal no problema | Pattern |
|-------------------|---------|
| Array sorted | Two Pointers / Binary Search |
| Subarray/substring | Sliding Window |
| Frequency/lookup | HashMap (Counter/defaultdict) |
| Shortest path / layers | BFS (deque) |
| Matching/nesting | Stack |
| Merge overlapping | Sort + merge intervals |

## Python Gotchas
- `def f(x=[])` → mutable default! Use `def f(x=None): x = x or []`
- `/` retorna float; use `//` para int division
- `sort()` in-place retorna None; `sorted()` retorna nova lista
- NUNCA `list.pop(0)` — use `deque.popleft()` (O(1) vs O(n))

---

# PREP SCHEDULE — Dia a Dia

## Sex 27/fev — Descanso + QA ML Início

| Horário | Atividade |
|---------|-----------|
| Manhã | Descansar. Debrief DoorDash. |
| Tarde (2-3h) | ML Clássico: revisar flashcards acima + quiz comigo (15 conceitos sem consulta) |
| Tarde (30min) | Esboçar business case: ranking de imóveis (cold start, features, modelo, métricas) |
| Noite | Descansar |

## Sáb 28/fev — QA ML Deep + Wise Coding

| Horário | Atividade |
|---------|-----------|
| Manhã (2h) | Deep Learning + GenAI + RAG deep dive + MLOps pipeline |
| Manhã (30min) | Desenhar ML pipeline completo no Figma/draw.io (praticar ferramenta!) |
| Tarde (1h) | Wise: implementar Circuit Breaker em Python (OOP, do zero, 3 test cases) |
| Tarde (1h) | Wise: implementar Rate Limiter simples (sliding window ou token bucket) |
| Noite | Descansar |

## Dom 1/mar — QA ML Final + Wise + Nubank Início

| Horário | Atividade |
|---------|-----------|
| Manhã (1h) | **Mock QA ML comigo** (perguntas técnicas + business case ranking imóveis) |
| Manhã (30min) | Feedback + rebuild gaps |
| Tarde (1h) | Wise: Currency Converter Python + Merge Intervals + SOLID de memória |
| Tarde (1h) | Nubank: Event-driven arch + Hexagonal + Event Sourcing (ler + desenhar) |
| Noite | Descansar cedo |

## Seg 2/mar — ENTREVISTA QA + Prep Wise/Nubank

| Horário | Atividade |
|---------|-----------|
| 11:00-11:30 | Revisão leve: flashcards ML + pipeline desenhado + 3 perguntas preparadas |
| 11:30 | Desabilitar IA, testar Google Meet, água, sala quieta |
| **12:00-13:00** | **QUINTOANDAR ML INTERVIEW** |
| 13:00-13:30 | Debrief: anotar o que caiu, o que foi bem/mal |
| 14:00-15:00 | **Mock pair programming Wise comigo** (problema surpresa, requirements mudam) |
| 15:00-16:00 | Nubank: desenhar Event Feed no Miro + trade-offs (Kafka vs SQS, sync vs async) |
| Noite | Descansar |

## Ter 3/mar — ENTREVISTA WISE + Prep Nubank

| Horário | Atividade |
|---------|-----------|
| 07:45-08:10 | SOLID de memória + `from collections import Counter, defaultdict, deque` + "Collaborate. Think aloud." |
| 08:10-08:25 | HackerRank CodePair testado, Python, sala quieta, água |
| **08:30-09:30** | **WISE PAIR PROGRAMMING** |
| 09:30-10:00 | Debrief Wise |
| 14:00-15:00 | **Mock Nubank Architecture comigo** (colaborativo, 2 eng, Event Feed ou Chargeback) |
| 15:00-16:00 | Feedback + rebuild + estudar Chargeback flow (FTP→CSV→validate→process→reconcile) |
| Noite | Descansar cedo |

## Qua 4/mar — ENTREVISTA NUBANK

| Horário | Atividade |
|---------|-----------|
| 09:00-09:30 | Revisão leve: padrões Nubank + números de escala + Miro testado |
| 09:30 | Lembrete: "Collaborate. Ask questions. Stop every 10 min to reassess." |
| **10:00-11:00** | **NUBANK ARCHITECTURE** |
| 11:00-11:30 | Debrief |
| Resto do dia | Descansar |

## Qui 5/mar — Circle (relaxar)

| Horário | Atividade |
|---------|-----------|
| TBD | **CIRCLE BATE-PAPO** (informal, sem prep) |
| Resto | Descansar. Semana acabou. |

---

# NAPKIN MATH — Quick Reference

| Metric | Value |
|--------|-------|
| 1 day | ~100K seconds (86,400) |
| 1M req/day | ~10 QPS |
| 1B req/day | ~10K QPS |
| 1 KB × 1M | 1 GB |
| 1 KB × 1B | 1 TB |
| Redis GET | ~0.1 ms (sub-ms) |
| DB query (indexed) | 1-10 ms |
| Postgres | 5-10K writes/sec |
| Redis | 100K+ ops/sec |
| Kafka | 1M msg/sec |

**Fórmulas:**
- QPS = total_diário ÷ 100K
- Peak = QPS × 3-5x
- Concurrent = total_diário × (duração_min / 1440)
- Storage/ano = registros × tamanho × 365

---

# REFERÊNCIA — Arquivos importantes

| Arquivo | Conteúdo |
|---------|----------|
| `companies/quintoandar/research.md` | Research completo QA (processo, stack, perguntas) |
| `companies/wise/research.md` | Research completo Wise (processo, problemas, stack) |
| `companies/nubank/research.md` | Research completo Nubank (processo, problemas, stack) |
| `prep/cheatsheet-sd.md` | SD cheatsheet (framework + problemas praticados DoorDash) |
| `prep/cheatsheet-leadership.md` | Leadership cheatsheet (STAR stories DoorDash) |
| `prep/compilado-sd-mocks.md` | Compilado mocks SD com correções |
| `notes.md` + `notes/` | Notas de estudo detalhadas (Kafka, Redis, patterns) |
| `MASTER-PREP.md` | Arquivo antigo consolidado (DoorDash + QA + Nubank) — SUPERSEDED por este arquivo |
