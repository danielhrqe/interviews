## Framework
| Fase | Tempo | O que fazer | Exemplo |
|------|-------|-------------|---------|
| 1a. Functional Req | 3min | O que o sistema FAZ | "Users can place orders, track delivery, leave reviews" |
| 1b. Non-Functional Req | 2min | Escala, latência, consistência | "How many users? Read/write ratio? Availability > consistency?" |
| 2. Napkin Math | 3min | QPS, storage → decide scaling | "10M orders/day = 100 QPS → single Postgres handles this" |
| 3. Core Entities | 3min | Tables + relationships | orders, users, items + FKs |
| 4. API Design | 5min | REST endpoints | POST /orders, GET /orders/:id |
| 5. High-Level | 5min | Components + arrows | Client → LB → API → Service → DB |
| 6. Deep Dive | 25min | 2-3 components, failure modes | Contention (OCC), caching, async flow |
| 7. Scaling | 10min | What breaks at 10x? | "Reads: add replicas. Writes: shard by X" |
| 8. Wrap-up | 4min | **3 comp + 2 trade-offs + 1 melhoria** | "Postgres SoT, Redis cache, Kafka events. Eventual on X, strong on Y. With more time: Z" |

## Napkin Math
| O que | Como | Exemplo |
|-------|------|---------|
| QPS | total/dia ÷ 100K | 10M orders → 100 QPS |
| Concurrent | total/dia × (dur_min / 1440) | 10M × (20/1440) = 140K |
| Peak | QPS × 3-5x | 100 × 5 = 500 QPS |
| Storage/dia | registros × tamanho | 10M × 0.5KB = 5GB |
| Storage/ano | storage/dia × 400 | 5GB × 400 = 2TB |
| Referência | Capacidade |
|------------|------------|
| Postgres | 5-10K writes/sec, 50K+ reads/sec |
| Redis | 100K+ ops/sec, sub-ms |
| Kafka | 1M+ msgs/sec por cluster |
| Row simples | ~0.5KB |
| Row c/ texto | ~1KB |
| 1 dia | 86,400 ≈ 100K seg |

## Problemas SD Praticados

| Problema | Componentes | Patterns | Deep Dive | Trade-offs & Scaling |
|----------|-------------|----------|-----------|----------------------|
| **Food Reviews + Payouts** | Postgres, Redis, Kafka, Queue+Worker | Async After 200, Outbox, Idempotency, DLQ | Vote: OCC/Redis INCR. Payout: saga+reconciliation | Eventual on counters, strong on payouts. Single PG. |
| **Donations Website** | Postgres, Stripe, Queue+Worker, Redis, DLQ | Async After 202, Idempotency, Reconciliation | Tx: create intent→confirm async. Campaign TTL. Counter: SSE | Avail > consistency counters. 0.03 QPS → trivial. |
| **Realtime Delivery Tracking** | Kafka (location), Redis (TTL 30s), WS Gateway | Fan-out Kafka consumers, Fallback to polling | WS: sticky sessions + conn registry. 140K concurrent. | OK lose GPS ping. Kafka-direct at WS for low latency. |
| **Local Delivery / Gopuff** | Postgres, Read Replicas, Avail Svc, Maps API | OCC (inventory race), Reservation + TTL | PostGIS + GiST index. OCC version column. | 0.1 QPS → single PG. No Kafka/ES needed. |
| **Job Scheduler** | Postgres, Queue, Workers, Redis (lock) | Partitioned sched, Idempotency, DLQ | Partition by time window. Heartbeat + lease timeout. | At-least-once + idempotency > exactly-once. |
| **Rate Limiter** | Redis (counters), API Gateway | Token Bucket (lazy refill, Lua) | Lua atomicidade. Fixed vs sliding window. | Approximate count ok. Redis cluster, shard user_id. |
