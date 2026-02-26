## Framework (60 min)

| Fase | Tempo | O que fazer | Exemplo / Referência |
|------|-------|-------------|----------------------|
| 1a. Functional Req | 3min | O que o sistema FAZ | "Users can place orders, track delivery, leave reviews" |
| 1b. Non-Functional Req | 2min | Escala, latência, consistência | "How many users? Read/write ratio? Availability > consistency?" |
| 2. Napkin Math | 3min | QPS = total/dia ÷ 100K. Concurrent = total/dia × (dur_min/1440). Peak = QPS × 3-5x. Storage = registros × tamanho × 400/ano. Refs: Postgres 5-10K w/s, Redis 100K ops/s, Kafka 1M msg/s. Row ~0.5KB. 1 dia ≈ 100K seg. | "10M orders = 100 QPS → single Postgres handles this" |
| 3. Core Entities | 3min | Tables + relationships | orders, users, items + FKs |
| 4. API Design | 5min | REST endpoints | POST /orders, GET /orders/:id |
| 5. High-Level | 5min | Components + arrows | Client → LB → API → Service → DB |
| 6. Deep Dive | 25min | 2-3 components, failure modes | Contention (OCC), caching, async flow |
| 7. Scaling | 10min | What breaks at 10x? | "Reads: replicas. Writes: shard by X" |
| 8. Wrap-up | 4min | **3 comp + 2 trade-offs + 1 melhoria** | "Postgres SoT, Redis cache, Kafka events. Eventual on X, strong on Y. With more time: Z" |

## Problemas SD Praticados

| Problema | Componentes | Patterns | Deep Dive | Trade-offs & Scaling |
|----------|-------------|----------|-----------|----------------------|
| **Food Reviews + Payouts** | Postgres (SoT, ACID), Redis (sub-ms counters w/ TTL), Kafka (ordered durable events), Queue+Worker | Async After 200, Outbox, Idempotency, DLQ | Vote: OCC/Redis INCR. Payout: saga+reconciliation | Eventual on counters, strong on payouts. Single PG. |
| **Donations Website** | Postgres (SoT, ACID), Stripe, Queue+Worker, Redis (cache w/ TTL), DLQ | Async After 202, Idempotency, Reconciliation | Tx: create intent→confirm async. Campaign TTL. Counter: SSE (server→client, auto-reconnect) | Avail > consistency counters. 0.03 QPS → trivial. |
| **Realtime Delivery Tracking** | Kafka (ordered durable location stream), Redis (latest state, TTL 30s), WebSocket Gateway (persistent conn, bidirectional push) | Fan-out Kafka consumers, Fallback to polling | WS: sticky sessions + conn registry. 140K concurrent. | OK lose GPS ping. Kafka-direct at WS for low latency. |
| **Local Delivery / Gopuff** | Postgres (SoT, ACID), Read Replicas, Avail Svc, Maps API | OCC (inventory race), Reservation + TTL | PostGIS + GiST index. OCC version column. | 0.1 QPS → single PG. No Kafka/ES needed. |
| **Job Scheduler** | Postgres (SoT), Queue, Workers, Redis (distributed lock, sub-ms) | Partitioned sched, Idempotency, DLQ | Partition by time window. Heartbeat + lease timeout. | At-least-once + idempotency > exactly-once. |
| **Rate Limiter** | Redis (counters, 100K+ ops/s), API Gateway | Token Bucket (lazy refill, Lua) | Lua atomicidade. Fixed vs sliding window. | Approximate count ok. Redis cluster, shard user_id. |
