# System Design - Prep Guide

> Priority: HIGHEST | DoorDash Round 1 on Feb 25 (60 min) | Also: Nubank, Wise, QA
> Sources: [DD research](../companies/doordash/research.md) sec 5, [EM Prep Kit](../companies/doordash/EM%20Interview%20Prep.pdf), [CTCI](../ctci-knowledge-base.md) sec 16

---

## 1. Universal 7-Step Framework (60 min)

| Step | Time | What to do |
|------|------|------------|
| **1. Requirements** | 5 min | Functional + non-functional. Ask: users, scale, latency, consistency needs |
| **2. Capacity Estimation** | 3 min | QPS, storage, bandwidth. Use napkin math below |
| **3. API Design** | 5 min | Core endpoints. REST verbs, params, responses |
| **4. Data Model** | 5 min | Entities, relationships, DB choice (SQL vs NoSQL), key indexes |
| **5. High-Level Architecture** | 10 min | Draw boxes: LB → App → Cache → DB → Queue. Data flow arrows |
| **6. Deep Dive** | 25 min | Interviewer picks 2-3 components. Go deep on trade-offs |
| **7. Scaling & Edge Cases** | 7 min | Bottlenecks, failure modes, monitoring, future evolution |

**DoorDash evaluation criteria** (from official prep kit):
- **Structure**: Systematic approach. Articulate WHAT and WHY
- **Comprehensiveness**: Cover all requirements + edge cases
- **Feasibility**: Practical, implementable solution
- **Scalability**: Capacity to grow with users/requirements

---

## 2. Napkin Math Cheat Sheet

### QPS Benchmarks
| Scale | Daily | QPS | Peak (3x) |
|-------|-------|-----|-----------|
| 1M users, 10 req/day | 10M | ~115 | ~350 |
| 10M users, 10 req/day | 100M | ~1,150 | ~3,500 |
| 100M users, 10 req/day | 1B | ~11,500 | ~35,000 |

### Conversion
- 1 day = 86,400 sec ≈ **100K sec** (for quick math)
- 1M req/day ≈ **12 QPS**

### Storage Sizes
| Data | Size |
|------|------|
| 1 char (UTF-8) | 1-4 bytes |
| UUID | 16 bytes |
| Timestamp | 8 bytes |
| Short text (tweet) | ~200 bytes |
| Image (compressed) | ~200 KB |
| Short video | ~5 MB |
| 1M users × 1 KB metadata | 1 GB |
| 1B rows × 1 KB | 1 TB |

### Latency Numbers
| Operation | Time |
|-----------|------|
| L1 cache ref | 0.5 ns |
| RAM access | 100 ns |
| SSD random read | 150 μs |
| HDD seek | 10 ms |
| Same-datacenter RTT | 0.5 ms |
| Cross-region RTT | 50-150 ms |
| Redis GET | 0.5-1 ms |
| DB query (indexed) | 1-10 ms |
| DB query (full scan) | 100ms-seconds |

---

## 3. Company-Specific Problem Bank

### DoorDash (PRIORITY - Round 1, Feb 25)

**1. Delivery Dispatch System** ⭐ Most likely
- Match orders with drivers in real-time
- Key: geospatial indexing (S2/H3 cells), regional sharding, event streaming (Kafka)
- Matching algorithms: greedy vs batched vs hybrid
- Target: <500ms assignment latency
- State machine: Order Created → Confirmed → Preparing → Assigned → Picked Up → Delivered
- Considerations: three-sided marketplace (customer, merchant, dasher)

**2. Real-Time Order Tracking**
- WebSocket connections for live updates, pub/sub (Kafka)
- Redis with geospatial indexes for driver locations
- Target: <200ms for location updates
- Client-side interpolation for smooth UI

**3. ETA Prediction Engine**
- ML model serving + feature stores + real-time inference
- Features: distance, traffic, restaurant prep time, historical data
- Ensemble approach: ML prediction + historical baseline
- Monitor model drift, fallback to simple estimates

**4. Restaurant Search Service**
- Full-text search (Elasticsearch), geolocation, ranking
- Personalization layer, cuisine filtering
- Caching popular queries, geo-based sharding

**Design patterns to mention for DoorDash:**
- Finite State Machine (order states)
- Event-Driven Architecture (Kafka)
- Circuit Breaker / Retry (driver offline → heartbeat → grace → reassign)
- CQRS (separate read/write paths)
- Rescue dispatch workflow

### Nubank

**1. Data Pipeline at Scale**
- ETL: Microservices → Kafka → Spark/Scala → S3 data lake
- Scale numbers: 1B events/day, ~100TB daily processing
- Immutability everywhere (Datomic, Kafka log, Clojure)
- Schema validation, incremental processing, deduplication

**2. Log Ingestion Platform**
- 1 trillion entries/day, 45 PB searchable
- Micro-batching with Fluent Bit → S3
- Cost vs query latency trade-offs

**3. Fraud Detection Pipeline**
- 450M events/day real-time processing
- Layered: rule engine + ML anomaly detection
- Stream processing, append-only audit trail
- Low latency critical (block transaction before it completes)

**Key Nubank design principles:**
- Hexagonal Architecture (ports and adapters)
- Idempotent message processing (correlate IDs)
- Logical and temporal decoupling via Kafka
- Functional programming as architectural principle

### Wise

**1. Money Transfer System**
- API Gateway → Transfer Service → Ledger → Currency Conversion → Notification
- Idempotency keys for every write operation
- Compliance: KYC/AML checks, audit trail
- Reconciliation between internal ledger and payout partners

**2. Internal Ledger Service**
- Double-entry bookkeeping, ACID guarantees
- Append-only for audit trails, event sourcing
- Multi-currency support, FX conversion records

**3. Exchange Rate Service**
- Rate ingestion from multiple providers
- Caching with consistency guarantees (stale rate → bad trade)
- Fallback mechanisms, latency optimization

**Key Wise design principles:**
- Consistency > Availability for core transactions
- Eventual consistency for non-critical (notifications, analytics)
- Immutable audit logs, event sourcing
- Simple, evolutionary architecture (start simple, iterate)

### QuintoAndar

**1. ML Pipeline / Feature Store**
- Templates padronizados → CI/CD → Databricks/Spark → Model Serving
- MLflow for experiment tracking
- Feature store for online/offline features
- Trunk-based development, 3-min deploy

**2. RAG System** (came up in Tech Screening - went well)
- Query → Embedding → Vector search → Top K docs → LLM → Response
- Tokenization before embedding
- Chunk strategy, retrieval quality metrics

---

## 4. Past Project Presentation Template (DoorDash 30-min Deep Dive)

DoorDash may ask you to present a past project with technical depth. Map to your **Platform story**.

### Structure (aim for 10-min presentation + 20-min Q&A)

**1. Context & Problem (2 min)**
- 5 platforms worldwide, no standardization, no governance
- 600+ engineers/DS needing a unified platform
- Concrete example: orphaned MongoDB in Mexico

**2. Architecture (3 min)**
- Azure: Databricks/Spark on K8s for compute
- Airflow for orchestration (4K+ DAGs)
- K8s + ArgoCD for model serving
- Terraform/Terragrunt for IaC
- Datadog for observability
- Azure Blob as data lake

**3. Key Decisions & Trade-offs (3 min)**
- Why Azure (enterprise agreement, existing investment)
- Template-based standardization vs flexibility trade-off
- Trunk-based development: speed vs risk
- Centralized vs federated data governance

**4. Results (2 min)**
- 70K+ executions/day, 150+ ML models in production
- 5 legacy platforms decommissioned
- Team grown from 1 to 9 engineers + 1 manager
- Global standard across all regions

**Prepare for these follow-up questions:**
- "What would you do differently?"
- "How did you handle data quality?"
- "How did you monitor models in production?"
- "What was the hardest technical challenge?"
- "How did you handle resistance to migration?"

---

## 5. Practice Protocol

### Timed Mock Structure
1. Set timer for 60 min
2. Read problem → spend EXACTLY 5 min on requirements (don't skip!)
3. 3 min estimation
4. 5 min API + data model
5. 10 min high-level diagram
6. 25 min deep dives (pick 2-3 components yourself)
7. 7 min scaling discussion
8. Stop. Review.

### Self-Evaluation Rubric

| Criterion | Strong | Weak |
|-----------|--------|------|
| Requirements | Asked 5+ clarifying Qs, identified non-functional reqs | Jumped straight to design |
| Estimation | Quick, reasonable numbers | Skipped or spent too long |
| Trade-offs | Explicitly stated 3+ trade-offs with reasoning | Picked options without explaining why |
| Depth | Deep-dived into 2+ components with implementation details | Surface-level everywhere |
| Communication | Structured, narrated decisions | Silent periods, jumped around |
| Scalability | Identified bottlenecks, proposed solutions | Didn't address growth |

### Practice Schedule (suggested)
- **Feb 13-14**: 1 mock/day (DoorDash-themed: dispatch, order tracking)
- **Feb 15-17**: 1 mock/day (general: URL shortener, Twitter, notification system)
- **Feb 18-21**: 1 mock/day (all companies: data pipeline, money transfer, ML pipeline)
- **Feb 22-24**: Past project presentation practice (record yourself, 3x)
- **Feb 25**: Light review, rest, interview day

---

## 6. Quick Reference: Common Components

| Component | When to use | Examples |
|-----------|-------------|---------|
| **Load Balancer** | Distribute traffic | L7 (ALB), L4 (NLB), round-robin, least-conn |
| **Cache** | Reduce DB load, low latency | Redis, Memcached. Strategies: cache-aside, write-through |
| **Message Queue** | Async processing, decouple services | Kafka (streaming), RabbitMQ (messaging), SQS |
| **CDN** | Static content, global distribution | CloudFront, Cloudflare |
| **Search** | Full-text, fuzzy, geo | Elasticsearch, Solr |
| **Object Storage** | Files, images, data lake | S3, Azure Blob, GCS |
| **SQL DB** | Structured data, ACID, joins | PostgreSQL, MySQL |
| **NoSQL DB** | Flexible schema, horizontal scale | DynamoDB, MongoDB, Cassandra |
| **API Gateway** | Auth, rate limiting, routing | Kong, API Gateway |
| **WebSocket** | Real-time bidirectional | Live tracking, chat |

### CAP Theorem Quick Reference
- **CP** (consistency + partition tolerance): Financial transactions, ledgers → PostgreSQL, DynamoDB (strong consistency mode)
- **AP** (availability + partition tolerance): Social feeds, location updates → Cassandra, DynamoDB (eventual)
- In practice: P is always present. Choose between C and A per use case, not globally
