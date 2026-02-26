# Compilado SD — O que errei e como deveria ter feito

---

## Mock #1: Food Reviews + Payouts (24/fev) — Borderline Hire (leaning Hire)

### O que fiz bem
- Entities e API design limpos
- Redis INCR para contadores de votos
- Separação de queues (votes vs payouts)
- DLQ e idempotency key mencionados

### O que errei e como corrigir

**1. Não fiz napkin math**
- Propus sharding sem calcular se precisava
- DEVERIA TER FEITO:
```
10M reviews/month → 330K/day → 3.3 QPS
Peak 5x → 16 QPS
→ Postgres single node aguenta FÁCIL (5-10K writes/sec)
→ NÃO precisa sharding no Day 1
```
→ Frase: "Let me do some quick math before designing... single Postgres handles this comfortably."

**2. Não vi o async critical path sozinho**
- User vota → eu botei tudo síncrono (write DB + update Redis + enqueue)
- DEVERIA TER DITO:
```
"The user doesn't need to wait for Redis or the queue.
Write to Postgres (source of truth) → return 200 →
fire-and-forget: update Redis counter + enqueue payout async."
```
→ Pattern: **Async After 200**

**3. Wrap-up vago nos trade-offs**
- Disse trade-offs genéricos sem conectar às decisões
- DEVERIA TER DITO:
```
"We chose eventual consistency on vote counts — Redis counter may lag
by a few seconds — for sub-100ms read responses.
But strong consistency on payouts via unique constraint + idempotency key,
accepting higher latency on that path."
```

---

## Mock #2: Donations Website (25/fev) — Hire (solid)

### O que fiz bem
- 7 trade-offs articulados com clareza (maior melhoria vs mock #1)
- Async After 202 aplicado corretamente sem dica
- DLQ + reconciliation mencionados proativamente
- Respondeu bem aos 3 pushbacks do entrevistador
- Scaling com números concretos para cenário 50x

### O que errei e como corrigir

**1. Napkin math — DE NOVO não fiz**
- DEVERIA TER FEITO:
```
2M users × 5% monthly = 100K/month ÷ 30 = 3,300/day
QPS = 3,300 / 100K = ~0.03 QPS
Peak 10x = ~0.3 QPS
→ TRIVIAL. Postgres dormindo.
```

**2. Wrap-up muito longo**
- Listei 10 componentes + 7 trade-offs + 5 melhorias (impossível em 60 segundos)
- DEVERIA TER DITO (formato 3+2+1):
```
"Three key components: Postgres as source of truth for donations,
a queue + worker for async payment processing with Stripe,
and Redis for caching charity pages and live counters.

Two main trade-offs: eventual consistency on donation counters
for fast reads, strong consistency on transactions via idempotency key.

With more time: I'd add read replicas and explore SSE
for real-time counter updates instead of polling."
```

**3. Live update mechanism vago**
- Mencionei Redis Pub/Sub para live counter mas não especifiquei como o frontend consome
- DEVERIA TER DITO: "SSE for unidirectional server-to-client updates on the donation counter. Simpler than WebSocket since we don't need bidirectional communication."

---

## Mock #3: Real-time Delivery Tracking (25/fev) — Borderline Hire

### O que fiz bem
- Arquitetura limpa: Driver → API → Kafka → Redis + WebSocket Gateway → Customer
- Data flows claros e bem separados
- Kafka partitioned by driver_id
- Redis TTL de 30 sec
- Regional topics como evolução

### O que errei e como corrigir

**1. Napkin math confuso e errado**
- Fiz contas que não conectavam entre si
- DEVERIA TER FEITO:
```
10M orders/day, active tracking ~20 min each
Concurrent deliveries = 10M × (20 / 1440) = ~140K simultaneous
Each driver pings every 3 sec → 140K / 3 = ~47K write QPS
Peak 3x = ~140K write QPS
Concurrent WebSocket connections = ~140K
```
→ Pattern: **concurrent = total_daily × (duration / 1440)**

**2. Deep dives rasos**
- "How to scale WebSocket?" → respondi "add more servers + K8s HPA"
- DEVERIA TER DITO:
```
"WebSocket is stateful — we need sticky sessions so the load balancer
routes to the right server. We maintain a connection registry
(Redis hash: order_id → server_id) so we know which server
holds each customer's connection.

For failover: if a server crashes, clients auto-reconnect.
On reconnect, they hit Redis for latest location, then
re-establish WebSocket. This is the fallback-to-polling pattern."
```

**3. Não articulei trade-off Kafka-direct vs Redis Pub/Sub**
- WebSocket Gateway consome direto do Kafka — entrevistador questionou
- DEVERIA TER DITO:
```
"Two options for pushing to WebSocket:
Option A: WS Gateway consumes Kafka directly — real-time, no extra hop,
but each server processes ALL messages and filters locally.
Option B: Location Processor writes to Redis, WS Gateway polls Redis —
simpler, but adds latency and polling overhead.

I'd go with Option A for latency requirements,
accepting the fan-out filtering cost."
```

**4. Não fiz wrap-up**
- DEVERIA TER DITO:
```
"Three key components: Kafka for durable, ordered location ingestion,
Redis for latest-state caching with TTL,
WebSocket Gateway for real-time push to customers.

Two trade-offs: availability over consistency — ok to lose a GPS ping,
and Kafka-direct consumption at WebSocket for lower latency
accepting higher processing per server.

With more time: location history storage for analytics,
ETA prediction based on location stream."
```

---

## Local Delivery Service / Gopuff (Hello Interview, ~22/fev)

### O que fiz bem
- Requirements claros: functional (query availability, order items) + non-functional (availability > consistency, strong on orders, <100ms)
- Scale definido: 10K DCs, 100K catalog items, 10K orders/day
- Entities bem modelados: distribution_centers, orders, order_item, inventory, products — schemas completos
- API design sólido: GET /availability com lat/long/radius, POST /order com items array
- Arquitetura limpa: Availability Service, Order Service, Delivery Estimated Service, Maps API, Postgres Primary + Read Replicas
- Separação read/write com replicas

### O que faltou vs referência

**1. Inventory Race Condition — NÃO mencionei**
- Problema: 2 users compram o último item ao mesmo tempo
- DEVERIA TER DITO:
```
"For inventory, I'd use optimistic locking with a version column:
UPDATE inventory SET reserved = reserved + 1, version = version + 1
WHERE product_id = ? AND store_id = ? AND quantity - reserved >= 1 AND version = ?
If affected_rows == 0, item is out of stock. No locks needed."
```
- Ou: Reservation pattern com TTL de 5 min (reserva → paga → confirma, se não paga, libera)

**2. Geospatial — muito vago**
- Mencionei Maps API mas não expliquei como encontrar o DC mais próximo
- DEVERIA TER DITO:
```
"For finding nearby DCs, I'd use PostGIS with a GiST index on the location column.
Query: ST_DWithin(dc.location, user_point, 5000) — finds DCs within 5km.
For sub-100ms, cache nearby DCs in Redis using GEOADD/GEORADIUS."
```

**3. Napkin math — não fiz (e teria justificado o design simples!)**
```
10K orders/day → 10K / 100K = 0.1 QPS (trivial!)
100K items × 500 bytes = 50MB total catalog
→ Single Postgres + read replicas resolve TUDO.
→ Kafka, Elasticsearch, Redis cache: DESNECESSÁRIOS nesse volume.
→ Design síncrono é a resposta CERTA aqui.
```
- A força está em DIZER isso: "I calculated 0.1 QPS — a single Postgres handles this comfortably. I don't need Kafka or a search engine at this scale."
- Isso demonstra senioridade: saber o que NÃO usar é tão importante quanto saber o que usar.

**4. Menções válidas para scaling futuro (mas não Day 1):**
- Se crescer 100x (1M orders/day = 10 QPS): ainda Postgres single node
- Se crescer 10,000x: aí sim Kafka para desacoplar, Elasticsearch para search, Redis para cache
- Na entrevista: "I'd mention these as evolution points, not Day 1 components"

---

## Gaps Recorrentes (DECORAR)

| # | Gap | Fix |
|---|-----|-----|
| 1 | **Não faz napkin math** | PRIMEIRO passo após requirements. Sempre. |
| 2 | **Wrap-up longo ou ausente** | Formato **3+2+1**: 3 componentes, 2 trade-offs, 1 melhoria |
| 3 | **Deep dive raso** | Não diga "add more servers". Diga: stateful vs stateless, connection registry, failover pattern |
| 4 | **Trade-offs genéricos** | Sempre conecte à decisão: "We chose X over Y because Z, accepting W" |

## Frase de Abertura (decorar)

Após requirements:
> "Before I start designing, let me do some quick math to understand the scale we're dealing with."

Após napkin math:
> "So we're looking at ~X QPS, which means [single Postgres handles this / we need distributed approach]. Let me design for this scale."
