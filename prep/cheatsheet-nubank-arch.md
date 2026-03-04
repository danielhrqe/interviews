## Framework Nubank (60 min — Miro, 2 eng, colaborativo, PORTUGUÊS)

| Fase | Tempo | O que fazer | Nubank Twist |
|------|-------|-------------|-------------|
| 1a. Requirements | 3min | O que o sistema FAZ | "Deixa eu garantir que entendi. Estamos construindo X para os 70M usuários." |
| 1b. Non-Functional | 2min | SLA, consistência, escala | Saldo = strong. Feed/extrato = eventual ok. Perguntar antes de assumir. |
| 2. Napkin Math | 3min | QPS = total/dia ÷ 100K. Peak = QPS × 3-5x. Refs: Postgres 5-10K w/s, Redis 100K ops/s, Kafka 1M msg/s. 70M users, 1B events/dia ≈ 12K/s, peak 50K/s | "57 QPS → Postgres ACID resolve. Não preciso de Saga." |
| 3. Core Entities | 3min | Entidades IMUTÁVEIS (append-only, Datomic-style) | Nunca DELETE. Novo fato com timestamp. Event sourcing natural. |
| 4. API / Events | 5min | REST sync + Kafka async. Outbox Pattern (DB + event mesma tx) | Event-driven > request-driven. CDC/poller publica no Kafka. |
| 5. High-Level | 5min | Service (Hexagonal) → Kafka → Consumer → DB | Port (REST) → Domain (logic) → Adapter (Datomic/Kafka). Domínio não conhece infra. |
| 6. Deep Dive | 25min | Idempotência, ordering, failure, DLQ | correlationId + dedup table. Kafka partition by user_id = ordem. DLQ após 3 retries. |
| 7. Scale + Failure | 10min | What breaks at 10x? Circuit breaker em deps externas | Kafka partitions ↑, consumer groups ↑. Fallback rules se modelo/serviço cai. |
| 8. Wrap-up | 4min | **3 comp + 2 trade-offs + 1 melhoria** | "Escolhi A, não B. Ganhei X, perdi Y." Concreto, nunca genérico. |

## Refs Throughput por Componente

| Componente | Writes/s | Reads/s | Nota |
|-----------|----------|---------|------|
| **Postgres** | 5-10K | 10-50K (replicas: 100K+) | ACID, strong consistency. Single node suficiente até ~10K w/s. |
| **DynamoDB** | 10-40K (auto-scale) | 10-100K (DAX cache: 1M+) | Key-value, eventual default. Partition key = distribuição. |
| **Redis** | 100K+ | 100K+ | In-memory, sub-ms. TTL. Cluster: 1M+ ops/s. |
| **Kafka** | 1M msg/s | 1M msg/s (consumer groups) | Durável, ordenado por partition. Partition by key = ordem garantida. |
| **Flink** | 1-10M events/s | — | Stream processing. State + checkpoint S3. Latência <100ms. |

## Problemas Praticados

| Problema | Componentes | Patterns | Deep Dive | Pattern Chave | Trade-offs & Scaling | Wrap-up 3+2+1 |
|----------|-------------|----------|-----------|--------------|----------------------|---------------|
| **Event Feed** | Kafka (partition user_id, ordered), Consumer idempotente (dedup table), DynamoDB (PK:user SK:ts) | Event Sourcing, Idempotência (event_id), DLQ | Kafka ordering por user. Consumer checa dedup antes de write. DLQ após 3 falhas. | Idempotência (correlationId + dedup table) | Eventual no feed, strong no saldo. W:10K R:1.4K → DynamoDB. Cache Redis top events. | **3:** Kafka, Consumer idempotente, DynamoDB. **2:** eventual feed vs strong saldo; DynamoDB vs Postgres (latência vs flex). **1:** cache Redis top events. |
| **Chargeback** | Postgres (ACID, state machine), Kafka (Outbox Pattern), Auto+Manual review | State Machine (OPENED→AUTO→MANUAL→RESOLVED), Outbox, DLQ | Auto-review corta 70% volume. Timeout automático. Notificação async. | State Machine + Outbox Pattern | 0.46 QPS → Postgres simples, NÃO Saga. Outbox garante consistência DB↔Kafka. ML scoring futuro. | **3:** State Machine, Outbox+Kafka, Auto+Manual review. **2:** ACID vs eventual (0.46 QPS justifica); auto-review 70%. **1:** ML fraud scoring. |
| **Pix Transaction** | Postgres (tx atômica, débito+crédito), Kafka pós-tx (extrato, notif), Outbox | ACID single tx (NÃO Saga, mesmo banco!), Outbox, Idempotency key | Uma transação atômica: débito + crédito + outbox. Kafka async pra extrato e notificação. | ACID single tx (NÃO Saga!) | 57 QPS → single Postgres. Eventual no extrato, strong no saldo. Rate limiting anti-fraude. | **3:** Postgres ACID, Kafka async, Outbox. **2:** single tx vs Saga (mesmo DB); eventual extrato vs strong saldo. **1:** rate limiting anti-fraude. |
| **Fraud Detection** | Flink (stream processing <100ms), Feature Store 2 camadas (Redis hist + Flink RT), Model + Fallback rules | Circuit Breaker + fallback, Features 2 camadas, DLQ | Flink scoring inline. Se modelo cai → circuit breaker → rules engine assume. Checkpoint S3. | Circuit Breaker + fallback rules | Latência vs accuracy (timeout 50ms). Flink vs Kafka Streams (state). 5.2K QPS. A/B test modelos. | **3:** Flink, Feature Store 2 camadas, Model+Fallback. **2:** latência vs accuracy; Flink vs Kafka Streams. **1:** A/B test modelos. |
