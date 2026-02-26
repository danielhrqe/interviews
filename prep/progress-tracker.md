# Progress Tracker — Interview Prep

> Atualizado: 24/fev/2026, 23h

---

## Countdown
| Entrevista | Data | Faltam |
|------------|------|--------|
| **DoorDash** — SD (60min) + Team Building (45min) | 26/fev 15h | **~1.5 dias** |
| **Wise** — Pair Programming (60min) | 27/fev 11h | **~2.5 dias** |
| **Nubank** — Architecture (60min) | 4/mar 10h | ~7 dias |
| **QuintoAndar** — ML Interview | ~3-6/mar | ~1-2 semanas |
| **QuintoAndar** — Coding (Codility) | ~9-13/mar | ~2-3 semanas |
| **Google** — 2x Coding/DSA | a agendar | semanas |

---

## System Design — Conceitos Estudados

### Ferramentas
| Ferramenta | Status | Nota | Gaps |
|------------|--------|------|------|
| **Kafka** | ✅ Estudado | 8/10 | Faltou: replication factor, leader/follower, exactly-once semantics |
| **Redis** | ✅ Estudado | 7/10 | Correções: sub-ms (não ms), TTL não é default (é eviction policy), hash slots (16384) |
| PostgreSQL | ✅ Sabe usar | — | Sabe read replicas, constraints, indexing |

### Decision Cards
| Ferramenta | Quando usar | Quando NÃO usar | Pitch |
|------------|-------------|------------------|-------|
| **Redis** | Cache, contadores, rate limiting, sessões, leaderboards, distributed locks | Durabilidade garantida, joins, datasets > memória | "I'd use Redis as a caching layer for sub-ms reads with TTL for staleness" |
| **Kafka** | Event streaming durável entre producers/consumers desacoplados | Request-response patterns, baixo volume | "I'd use Kafka to decouple this service and guarantee ordered, durable event delivery" |

### Padrões de Design
| Padrão | Status | Nota | Gaps |
|--------|--------|------|------|
| **Multi-step Process** | ✅ | 8/10 | Faltou: compensating transactions |
| **Contention** | ✅ | 9/10 | Faltou: 2PC coordinator failure como trade-off |
| **Rate Limiter** | ✅ | 7/10 | Token bucket precisa ficar mais fluente |
| **Outbox Pattern** | 🟡 Aprendeu no mock | — | Memorizar: write + event na mesma transaction, poller publica |
| **Async after 200** | 🟡 Aprendeu no mock | — | Memorizar: "write source of truth, return 200, rest is async" |
| **Saga Pattern** | ✅ | — | Sabe conceito, usar para microservices distribuídos |
| **2PC** | ✅ | — | Sabe conceito, NÃO recomendado para microservices |
| CAP Theorem | ✅ | — | — |

### Problemas SD Praticados
| Problema | Status | Como estudou | Nota |
|----------|--------|-------------|------|
| **Food Reviews + Payouts** | ✅ Mock feito (24/fev) | Mock com Claude | **Borderline Hire (leaning Hire)** |
| **Food Reviews** | ✅ Mock Hello Interview (23/fev) | Hello Interview | Feedback perdido (queda de luz) |
| **Job Scheduler** | ✅ Estudado (24/fev manhã) | Hello Interview + notas | 8/10 — faltou partitioned scheduling, DLQ |
| **Rate Limiter** | ✅ Estudado | Hello Interview + notas | 7/10 |
| **Uber/Ride Matching** | 🟡 Estudado (básico) | Hello Interview + notas | 5/10 — faltou geospatial indexing |
| **Donations Website** | ✅ Mock feito (25/fev) | Mock com Claude | **Hire (solid)** — trade-offs excelentes, faltou napkin math |
| **Local Delivery Service** | ✅ Estudado | Hello Interview | — |
| **Real-time Delivery Tracking** | ✅ Mock feito (25/fev) | Mock com Claude | **Borderline Hire** — arch boa, napkin math errado, faltou wrap-up |

---

## System Design — Gaps Recorrentes (PRIORIDADE)

### 1. Napkin Math — Sabe o conceito, erra zeros
- Drill feito (25/fev): 9 exercícios, lógica 9/9 correta, zeros 3/9 corretos
- **Problema específico**: manipulação de ordens de grandeza (K×M, B/100K)
- Sabe: atalho 86,400≈100K, QPS=total/100K, storage=registros×tamanho×365
- **Precisa**: escrever unidades no papel e cancelar (M×KB=GB)
- **Regra**: sempre pergunte os números, faça as contas, SÓ DEPOIS proponha escalabilidade

### 2. Async Critical Path — Não viu sozinho
- Em fluxos de vote/write, o user NÃO precisa esperar Redis + Queue
- **Memorizar**: "Write to source of truth → return 200 → fire-and-forget the rest"
- Outbox pattern para garantir que eventos não se percam

### 3. Wrap-up / Trade-offs — Vago
- Precisa articular trade-offs com clareza: "We chose X over Y because Z, accepting W as a cost"
- Exemplo bom: "Eventual consistency on vote counts for sub-100ms responses. Strong consistency on payouts via unique constraint, accepting higher latency."

### 4. Communication Structure
- Usar "there are N things: first... second... third..." para organizar respostas
- Não pular direto para a solução sem explicar o raciocínio

---

## Team Building & Hiring (DoorDash)

| Item | Status |
|------|--------|
| 6 STAR stories escritas | ✅ |
| Mock #1 (19/fev) | Borderline — faltou contexto, números, diversidade |
| Mock #2 (19/fev) | **Hire (borderline Strong Hire)** |
| Diversidade (4/7 promoções Black/Brown) | ✅ Resposta reconstruída |
| 5 Key Numbers memorizados | Revisar |

---

## Wise — Pair Programming

| Item | Status |
|------|--------|
| Research completo | ✅ (companies/wise/research.md) |
| Problemas conhecidos | Currency Converter, Circuit Breaker, Rate Limiter, Sorting Intervals |
| Foco da entrevista | Colaboração, clean code, comunicação, OOP |
| Platform | HackerRank CodePair |
| Language | Java primary (confirmar se Python ok) |
| Prática de problemas | ❌ NÃO FEZ AINDA |

---

## Coding — Nível Geral (diagnóstico 11/fev)

| Tópico | Nível | Atualização |
|--------|-------|-------------|
| Big O | Bom- | — |
| HashMap | Bom- | Melhorou com prática SD |
| Two Pointers | Básico | — |
| Sliding Window | Básico | — |
| Stacks | Básico | — |
| Binary Search | Estudar | — |
| Trees/BST | Básico | — |
| BFS/Grid | Estudar | — |
| Sorting | Básico | — |
| Python ref/copy | Fraco | — |
| Collections | Estudar | — |
| Functional | Bom- | — |