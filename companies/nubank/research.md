# Nubank Interview Research: Systems Engineer / Data Infrastructure (IC7)

> Compiled: 2026-02-10 | Sources: Glassdoor, Hacker News, Building Nubank blog, GitHub, Levels.fyi, Prepfully

---

## 1. Interview Process - All Stages

The process takes **35-45 days on average** and has 5-6 stages:

### Stage 1: Application & Screening (~1 week)
- Online application form
- Remote interview with recruiter OR engineer
- Behavioral + technical questions: decision-making, experience, salary expectations
- Cultural fit assessment, diversity values

### Stage 2: Take-Home Technical Exercise (~5-10 days to complete)
- You receive a coding problem to solve in **your preferred language**
- Simulates real problems Nubank faces
- You DON'T need to finish -- they evaluate **how you think, approach problems, and communicate reasoning**
- They look at: clean code, organized structure, readability, trade-off decisions
- This exercise may be reused in the pair programming stage

### Stage 3: Pair Programming (live, ~1-2 hours)
- You + **two Nubank engineers** work together
- Either extend the take-home solution OR tackle a new problem
- Done on **HackerRank** (CodeSignal for interns)
- They evaluate: collaboration, explaining reasoning, receiving feedback, adaptive problem-solving
- NOT a "gotcha" test -- they value discussion and curiosity

### Stage 4: Architecture Round (SENIOR/STAFF ONLY)
- Whiteboard-style system design
- Focus: complex, scalable, and resilient systems
- Conversational -- you discuss a business problem and design a system
- They want to see trade-off reasoning (complexity, performance, cost, simplicity)
- Knowledge of asynchronous communication and key AWS services mentioned

### Stage 5: Engineering Interview
- Deeper dive into algorithms, logic, and system design
- More technical depth than pair programming

### Stage 6: People & Culture + Leadership Interview
- Values alignment, collaboration style, how you work in teams
- Interview with engineering leadership (practically means you're close to an offer)

**Before each stage**, candidates receive a PDF describing exactly what to expect.

---

## 2. Coding Format & Language

### Platform
- **HackerRank** for live pair programming sessions
- **CodeSignal** for intern-level coding assessments
- Take-home exercise: any IDE, your own environment

### Language
- **You can use any language you're comfortable with** for the take-home and pair programming
- Nubank internally uses **Clojure** (1000+ microservices), **Scala** (data processing/Spark), and some Python
- 99% of engineers who join had **never used Clojure before** -- they train you
- For the take-home, **functional programming languages are preferred** for some challenges (Clojure, Haskell, Elixir, Scala accepted)
- **Python is acceptable** and commonly used by candidates
- IMPORTANT: One candidate was rejected for using a database instead of in-memory collections -- they wanted to see functional programming patterns (map/filter/reduce)

### What They Look For in Code
1. Clean, readable code (code should "speak for itself")
2. Descriptive variable/function names
3. Small functions with well-defined responsibilities
4. No dead code, no unnecessary comments
5. No external libraries beyond what's provided
6. Logic and data structure understanding over raw coding speed
7. Pseudocode first, then implement

---

## 3. Known Coding Challenges (Specific Problems)

### Challenge A: Capital Gains Tax Calculator (CURRENT/RECENT)
**The most commonly reported take-home challenge.**

- CLI application that processes stock buy/sell operations and calculates taxes
- Input: JSON via stdin with operations `{"operation":"buy/sell", "unit-cost":X, "quantity":Y}`
- Output: JSON with tax for each operation `{"tax":0.00}`
- Rules:
  - 20% tax on profit
  - No tax if total operation value <= R$20,000
  - No tax on buy operations
  - Past losses must be deducted from future profits
  - Weighted average price: `((current_qty * current_avg) + (bought_qty * buy_price)) / (current_qty + bought_qty)`
- Multiple implementations on GitHub (Python, Kotlin, Rust, etc.)
- Difficulty: **Medium** -- not algorithmically hard, but tests clean code and edge cases

### Challenge B: Job Queue with Precedence Rules
**Classic Nubank challenge (still reported).**

- Two entities: Jobs (id, type, urgency flag) and Agents (id, primary skills, secondary skills)
- Implement a dequeue function following precedence rules:
  - Jobs ordered by arrival time (FIFO)
  - Urgent jobs have priority
  - Agent can only get jobs matching their skill sets
  - Agent gets secondary skill jobs only if no primary skill jobs available
  - Job is "done" when agent requests a new job
- Input: sample-input.json via stdin -> Output: sample-output.json via stdout
- Part 2: Convert to REST API maintaining state between calls
- **Key trap**: Use in-memory data structures (atoms/collections), NOT a database. They want functional programming patterns.
- Difficulty: **Medium**

### Challenge C: URL Shortener
**Reported in pair programming sessions.**

- Develop an app for shortening links and listing them
- TDD is valued
- Pair programming extends the basic solution

### Challenge D: HackerRank Live Coding (Pair Programming)
- **LeetCode Easy level** problems
- Focus on basic data structures: **lists, dictionaries** (NOT linked lists, binary trees)
- ~50 LeetCode Easy problems is sufficient preparation
- 2-3 problems in a session

---

## 4. Difficulty Level

| Source | Rating |
|--------|--------|
| Glassdoor average | 3.23 / 5.0 |
| Senior SWE specifically | 3.3 / 5.0 |
| Take-home challenge | Medium (clean code > algorithm complexity) |
| Live coding (pair programming) | **LeetCode Easy** |
| Architecture round | Medium-Hard (system design) |

**Key insight**: Nubank interviews are NOT LeetCode-grinding style. They are more practical/applied. The difficulty comes from:
- Writing clean, production-quality code under observation
- Communicating trade-offs clearly
- Functional programming mindset
- System design breadth for senior roles

---

## 5. Topics That Come Up Frequently

### Coding
- Basic data structures: **lists, dictionaries/hash maps, queues**
- JSON parsing (stdin/stdout)
- State management (in-memory)
- Weighted averages, financial calculations
- FIFO queues with priority
- Map/filter/reduce operations
- Clean code principles
- TDD (Test-Driven Development)
- Edge case handling

### System Design / Architecture
- Microservices architecture
- Asynchronous communication (Kafka, message queues)
- Event-driven architecture
- Scalability and resilience
- Trade-offs: consistency vs availability
- AWS services knowledge
- API design (REST)
- Database choices and trade-offs

### Behavioral / Culture
- How you make decisions
- Collaboration and teamwork examples
- Handling disagreements
- Product vision
- Diversity and inclusion values

---

## 6. Data Infrastructure Specific

### Nubank's Data Infra Tech Stack
| Technology | Use Case |
|-----------|----------|
| **Apache Spark** | Core data processing (batch) |
| **Scala** | Spark jobs, data transformations |
| **Clojure** | Microservices |
| **Kafka** | Event streaming, async communication |
| **AWS S3** | Data lake storage |
| **Databricks** | Spark cluster management |
| **DynamoDB** | NoSQL database |
| **PostgreSQL** | Relational database |
| **Datomic** | Immutable database (append-only) |
| **Airflow** | Workflow orchestration |
| **Mesos/Aurora** | Container orchestration (legacy) |
| **Tekton** | CI/CD pipelines |
| **Prometheus** | Monitoring |
| **Splunk** | Logging |

### Scale Numbers
- 59+ million users
- 1 billion triggered events per day
- ~100 TB of event data processed daily
- 1 trillion log entries daily (1 PB/day)
- 45 PB of searchable log data
- 450 million events/day on fraud defense platform
- 5 million internal requests per minute
- 1000+ Clojure microservices
- 20 deploys per day

### Data Architecture
- ETL: Extraction (from microservices) -> Transformation (Spark/Scala) -> Loading (S3)
- Contracts: Scala objects auto-generated from service data models
- Event deduplication at message broker level
- Incremental daily processing (not full reprocessing)
- Schema validation for data ingestion
- Automated data versioning in Data Lake

### What They'd Ask a Data Infra Candidate
- Experience building/operating large-scale distributed data processing
- Deep understanding of Spark, Kafka Streams, Flink
- Infrastructure as code
- Monitoring and observability for data pipelines
- Production-ready services
- Experience with high stability requirements
- Abstracting complexity from internal users (self-service platform)

---

## 7. System Design Topics for Data Infra

Based on Nubank's actual architecture, likely system design topics include:

1. **Design a self-service data processing platform** (their actual product)
2. **Design a log ingestion pipeline** (1 trillion entries/day, 45 PB retention)
3. **Design an event-driven microservices system** with Kafka
4. **Design a fraud detection pipeline** (real-time, 450M events/day)
5. **Design a data lake with ETL** (S3, Spark, schema validation)
6. **Design an observability/monitoring platform** (micro-batching, Fluent Bit, S3)
7. **Design a financial transaction processing system** (immutability, audit trail, Datomic)

### Key Architecture Principles at Nubank
- **Immutability everywhere** (Datomic append-only, Kafka immutable log, Clojure immutable data)
- **Hexagonal Architecture** (ports and adapters)
- **Idempotent message processing** (correlate IDs for deduplication)
- **Logical and temporal decoupling** via Kafka
- **Horizontal scalability** (spin up entire production stacks, DNS switching)
- **Functional programming** as architectural principle

---

## 8. Blog Posts & Experience Reports

### Official Nubank Blog (building.nubank.com)
- [What is the hiring process like for Software Engineers?](https://building.nubank.com/what-is-the-interview-process-like-for-software-engineers-at-nubank/)
- [8 tips to solve software engineering technical exercise](https://building.nubank.com/tips-software-engineering-technical-exercise/)
- [How Nubank uses Spark to process data](https://building.nubank.com/how-nubank-uses-spark-to-process-data/)
- [Scala Hands-On: building queries in Spark](https://building.nubank.com/scala-hands-on-a-path-to-build-and-manage-queries-in-spark/)
- [Microservices at Nubank overview](https://building.nubank.com/microservices-at-nubank-an-overview/)
- [Functional programming with Clojure](https://building.nubank.com/functional-programming-with-clojure/)
- [How Nubank built its in-house log platform](https://building.nubank.com/how-nubank-built-its-in-house-log-platform/)
- [Scaling fraud defense](https://building.nubank.com/scaling-fraud-defense-how-nubank-evolved-its-risk-analysis-platform/)
- [Acing Nubank's technical exercise (Part 1)](https://medium.com/building-nubank/acing-nubanks-technical-exercise-part-1-59c8a6d3829d)

### Candidate Reports
- [Hacker News: Rejected from Nubank](https://news.ycombinator.com/item?id=16412577) - Job queue challenge, rejected for using DB instead of in-memory collections
- [NuShop experience report](https://www.abilioazevedo.com.br/posts/nushop-processo-seletivo-nubank) - URL shortener + TDD pair programming, good feedback on communication
- Glassdoor: 1,170+ interview questions, 1,150+ reviews

---

## 9. Patterns for Senior IC Levels (IC7/Staff)

### IC7 at Nubank
- Maps roughly to "Staff Engineer" externally
- Compensation: ~R$694K/year (Brazil) or ~EUR 163K/year (Germany)
- IC7 is labeled "E4" internally (IC7/E4)
- Expected: 12+ months at Nubank for internal moves (suggests high bar for external hires)

### What's Different for Senior/Staff
1. **Architecture round is mandatory** (not required for junior levels)
2. **System design is conversational** -- discuss business problems, not whiteboard algorithms
3. **Trade-off reasoning** is heavily weighted (complexity, performance, cost, simplicity)
4. **Scope of impact** matters -- they want to see cross-team influence
5. **AWS knowledge** is expected (their entire infra runs on AWS)
6. **Asynchronous communication patterns** knowledge required
7. **Production experience at scale** -- they care about operating systems, not just building them
8. The process may be longer (~45 days for senior vs ~35 days average)

### Red Flags That Get Seniors Rejected
- Over-engineering the take-home (using DB when they want simplicity)
- Not explaining trade-offs in architecture discussions
- Poor collaboration during pair programming
- Cultural fit issues (even with strong technical skills)
- Not asking questions during the process

---

## 10. Preparation Recommendations for Data Infra IC7

### Coding Prep (Lower Priority)
- ~50 LeetCode Easy problems (lists, dicts, basic logic)
- Practice JSON stdin/stdout processing in Python
- Practice writing clean, well-structured code with good naming
- Implement a simple financial calculator (weighted averages, tax rules)
- Practice TDD workflow

### System Design Prep (HIGH Priority)
- Study Nubank's architecture blog posts (especially Spark, Kafka, logging platform)
- Practice designing: event-driven systems, data pipelines, log ingestion at scale
- Know Kafka deeply (partitioning, consumer groups, exactly-once, idempotency)
- Know Spark internals (driver/executor, partitions, shuffle, AQE)
- AWS services: S3, DynamoDB, EKS/Kubernetes
- Hexagonal architecture pattern
- Immutability as an architectural principle

### Cultural Prep
- Prepare examples of cross-team collaboration
- Think about how you'd build self-service platforms
- Have opinions on functional programming (even if you use Python)
- Show curiosity -- ask lots of questions during interviews
- Prepare examples of trade-off decisions you've made

### Functional Programming Basics
Even if you code in Python, understand:
- Pure functions (no side effects)
- Immutable data structures
- Map/filter/reduce patterns
- Why these matter for financial systems (auditability, reproducibility)

d---

## 11. Teste de Lógica - CodeSignal GCA (atualizado 11/fev)

> Fonte: email oficial do Nubank + pesquisa CodeSignal + relatos candidatos

### Formato
- **Plataforma:** CodeSignal (app.codesignal.com)
- **Tipo:** GCA (General Coding Assessment) - é CODING, não multiple choice
- **4 questões**, **70 minutos** total
- **Proctored:** webcam, tela compartilhada, RG, sem consulta, sem sair
- **Linguagem:** escolha livre (Python ok)
- **Deadline:** 14/fev/2026

### Estrutura das Questões

| Q | Dificuldade | Tempo | Tipo |
|---|------------|-------|------|
| Q1 | Easy | ~5 min | Array/string simples |
| Q2 | Easy-Medium | ~10 min | String/implementação |
| Q3 | Medium (longo) | ~25 min | Implementação pesada (matrix, simulação) |
| Q4 | Medium-Hard | ~25 min | Algorítmico (HashMap, prefix sum) |

### DICA CRÍTICA: Ordem 1 → 2 → 4 → 3
Q4 vale mais que Q3 por tempo investido. Q3 é longa mas straightforward.

### Tópicos que caem
- Arrays, strings, sliding window, hashmaps (mais comuns)
- Matrix/2D traversal (Q3 geralmente)
- Prefix sums, two pointers, sorting
- **DP NÃO cai** (confirmado por múltiplas fontes)

### Questões reais reportadas
- Q1: Sliding triplet sum (`b[i] = a[i-1] + a[i] + a[i+1]`)
- Q2: Vowel/consonant pattern matching
- Q3: Tetris drop simulation / Matrix submatrix sums
- Q4: Contar pares cuja soma é potência de 2 (HashMap)

### Preparação
1. Criar conta CodeSignal e fazer practice assessment (empresa não vê)
2. Baixar Cosmo app (prática CodeSignal)
3. LeetCode Easy/Medium: arrays, strings, hashmaps, sliding window
4. Simular 70 min cronometrado
5. Partial credit é generoso - sempre submeta algo
6. Máx 2 tentativas por 30 dias
