# Nubank Architecture — Problemas para Praticar

## Formato: 1h, Miro, 2 eng, colaborativo, processo > resultado

## Problemas (ordem de prioridade)

### 1. Event Feed (MAIS COMUM) ⭐⭐⭐
**Cenário:** Design a system that shows users their financial activity feed (Pix sent, card purchase, refund, bill payment). 70M users, ~12K events/sec.
**Core:** Kafka → Consumer → Datomic → Read API
**Follow-ups:** Ordering guarantees, idempotency, real-time push notifications, search/filter

### 2. Chargeback/Dispute System ⭐⭐
**Cenário:** User disputes a credit card charge. Design the workflow from dispute creation to resolution. Must handle: merchant notification, temporary credit, investigation, final resolution.
**Core:** State machine (OPENED→INVESTIGATING→RESOLVED), Saga pattern, notifications
**Follow-ups:** Timeout automático, partial refund, fraud correlation, audit trail

### 3. Transaction Processing ⭐⭐
**Cenário:** Process a Pix transfer: validate sender balance, debit sender, credit receiver, notify both. Must be exactly-once. 5M transactions/day.
**Core:** ACID for balance, Saga for cross-service, idempotency key
**Follow-ups:** Double-spend prevention, international transfers, rate limiting, reconciliation

### 4. Fraud Detection Pipeline ⭐
**Cenário:** Score every transaction for fraud risk in <100ms. 450M events/day. Must not block legitimate transactions.
**Core:** Kafka Streams → Feature lookup → Model scoring → Decision (block/allow/review)
**Follow-ups:** False positive handling, model update without downtime, circuit breaker for model service

### 5. Redesign Existing Architecture ⭐
**Cenário:** "We have a monolithic billing service that's becoming a bottleneck. How would you break it into microservices?"
**Core:** Domain decomposition, strangler fig pattern, event-driven migration
**Follow-ups:** Data migration strategy, backward compatibility, rollback plan

## Patterns para TODOS os problemas
- Event Sourcing (append-only, replay)
- Idempotência (correlationId + dedup table)
- DLQ (3 retries → dead letter → alert)
- Hexagonal (ports + adapters)
- Imutabilidade (Datomic-style, never delete)
- Outbox Pattern (DB write + event in same tx)
- Circuit Breaker (stop cascading failures)
