# Wise (formerly TransferWise) Interview Research: Staff SWE / Engineering Lead

> Compiled: 2026-02-10 | Updated: 2026-02-20
> Sources: Glassdoor, Blind, LeetCode Discuss, Wise Careers Blog, Wise Engineering Blog, Educative, SystemDesignHandbook, InterviewQuery, Prepfully, Levels.fyi, The Pragmatic Engineer
> Career Map: https://wise.jobs/engineering-career-map

## 0. Status & Path Options

**Conversa com Director of Engineering (20/fev):** Muito boa. Aguardando agendamento das próximas etapas.

Duas possibilidades:
- **Engineering Lead (EL1/EL2)** — Manager track
- **Staff Engineer (IC5)** — IC track

### Engineering Lead 1 (EL1) — £100K-125K
- Escopo: 1 time, dono do domínio
- Dono do roadmap técnico do time (tech debt, reliability, security, scalability)
- Contribui ativamente na execução do dia-a-dia
- Gerencia performance e wellbeing dos engenheiros
- Faz entrevistas (~2 candidatos/semana)
- Expertise técnica mínima: IC3

### Engineering Lead 2 (EL2) — £125K-153K
- Escopo: 1+ times, líder confiável cross-functional
- Contribui para visão e estratégia
- Dono de roadmaps de produto + técnicos
- Times entregam com qualidade **sem envolvimento diário** dele
- Planeja crescimento do time com milestones executáveis
- Expertise técnica mínima: IC4

### Staff Engineer IC5 — £130K-164K
- Escopo: múltiplos domínios, altamente autônomo
- Dono de visão/estratégia técnica e de produto de uma área grande
- Identifica os problemas de maior impacto
- Dono do roadmap da disciplina técnica **na organização toda**
- Lidera resolução de incidentes graves (mesmo fora do domínio)
- Mentora pipeline de IC5+
- Contribui externamente (talks, blog posts)

---

---

## 1. Interview Process - All Stages

The process takes approximately **30-45 days** and typically has **5 stages** for Staff-level positions:

### Stage 1: Recruiter Screening (~30 minutes)
- Phone/video call with a recruiter
- Topics: your background, motivations, knowledge of Wise, salary expectations
- The recruiter explains the full hiring process and next steps
- They assess basic cultural alignment and communication
- **Tip**: Research Wise's mission ("Money without borders"), understand their fee model and borderless account product

### Stage 2: Pair Programming / Coding Interview (~60 minutes)
- Conducted on **HackerRank CodePair** (interactive collaborative coding platform)
- Can be onsite or via Zoom
- Primary language: **Java** (some teams accept other languages -- confirm with recruiter)
- Includes a brief introduction and 5 minutes for candidate questions at the end
- **NOT a traditional LeetCode grind** -- problems tend to be practical/domain-relevant
- You and the interviewer solve a problem together collaboratively

### Stage 3: System Design Interview (~90 minutes)
- Two parts: (1) discussion about your experience + technical questions, (2) system design task
- The system design task takes the majority of the time
- Conducted via Google Meet or onsite, using collaborative whiteboard tools (HackerRank)
- Focus: designing performant, maintainable, extensible systems for real-world problems
- For Staff level: expect deep dives into data consistency, distributed systems, and financial domain

### Stage 4: Product Interview
- Evaluates your **product mindset** -- a core Wise engineering value
- Focus: understanding customer problems, prioritization, measuring success, iterating
- Questions like: How would you measure if a feature is successful? How do you prioritize between new features vs. tech debt?
- Engineers at Wise are expected to have opinions about WHAT to build, not just HOW
- No single "right" answers -- they want structured thinking backed by data/arguments

### Stage 5: Team & Culture / Hiring Manager Interview
- Meet the team you would work with, including your potential lead/manager
- Open-ended and scenario-based questions
- Assessment of decision-making, work style, values alignment
- Behavioral questions using STAR method (Situation, Task, Action, Result)
- This is where they assess leadership qualities for Staff level

**Note**: Some candidates report variations in order. For senior roles, there may also be a technical round of ~1.5 hours with 3 panelists covering behavioral, team lead skills, project estimation, and design.

---

## 2. Coding Interview Format

### Platform
- **HackerRank CodePair** for live pair programming sessions
- HackerRank also used for initial online assessments (for some roles/levels)

### Language
- **Java is the primary language** -- Wise's backend is almost entirely JVM-based (Java + some Kotlin)
- Some teams accept Python, Kotlin, or other languages -- **confirm with your recruiter in Stage 1**
- If you use Python, be prepared that interviewers may be less familiar with it

### What They Evaluate (4 Dimensions)
1. **Collaboration & Communication** -- How you work with the interviewer, explain your reasoning, ask clarifying questions
2. **Architecture** -- Decision-making rationale, code organization, trade-off analysis
3. **Problem Solving** -- Approach to non-trivial problems within time constraints
4. **Code Quality** -- Clarity, testability, readability (SOLID, DRY, KISS principles)

### What IS Covered
- Algorithms and data structures
- Space/time complexity analysis
- Concurrency concepts (ConcurrentHashMap, thread safety)
- Language-specific features (Java: generics, streams, exceptions, memory management)
- Industry coding practices (SOLID, DRY, KISS)

### What is NOT Covered
- System design (separate interview)
- Riddles or trick questions
- Deep dives into past experience (separate stage)

### Interview Style
- **Pair programming**: the interviewer collaborates with you, not just watches
- Start by understanding the problem, ask clarifying questions
- Explain your thought process aloud ("provide a narrative as you go")
- Consider multiple algorithmic approaches before coding
- The interviewer is there to help -- ask questions and discuss

---

## 3. Known Coding Problems (From Candidate Reports)

### Problem A: Currency Converter / Exchange
- Implement an interface for currency exchange
- Given two methods for sending and receiving money
- Refactor code based on edge cases (e.g., ensure receiver exists, has an account)
- Domain-relevant to Wise's actual business
- Difficulty: **Easy-Medium**

### Problem B: Circuit Breaker Pattern
- Implement a circuit breaker: if a service fails 3 times within 10 minutes, stop requests for 5 minutes
- After 5 minutes, resume attempts
- Implemented in a `WebClient.execute(Request)` method
- Tests: OOP design, state management, time-based logic
- Difficulty: **Medium**

### Problem C: Rate Limiter (reported as similar to LC Medium)
- Design and implement a rate limiter
- Tests: concurrency, data structures, clean code
- Difficulty: **Medium**

### Problem D: Sorting Two Lists of Intervals
- Merge or sort two lists of time/value intervals
- Classic interval problem with practical application
- Difficulty: **Medium**

### Problem E: Best Exchange Rate (from TransferWise Coding Contest)
- Find the best exchange rate between two currencies
- Build a directed graph (currencies as nodes, rates as edges)
- Graph traversal to find optimal conversion path
- Difficulty: **Medium**

### Problem F: Java Code Fluency Exercise
- Not algorithm-focused; more about writing clean Java code in a collaborative environment
- Tests practical coding ability and Java proficiency
- Difficulty: **Easy-Medium**

### Online Assessment (Graduate/Some Roles)
- 2 questions in 75 minutes on HackerRank
- One data structures & algorithms question
- One RESTful API question
- **Note**: Staff level likely skips the OA and goes straight to pair programming

---

## 4. Difficulty Level

| Component | Difficulty |
|-----------|-----------|
| Glassdoor average rating | 3.2 / 5.0 |
| Pair programming coding | **LeetCode Easy-Medium** |
| System design | **Medium-Hard** (financial domain adds complexity) |
| Product interview | N/A (no "right" answers) |
| Overall process | More practical than algorithmic |

### Key Insight
Wise interviews are **NOT LeetCode-grinding style**. They prioritize:
- Practical, domain-relevant problems over abstract puzzles
- Clean, readable code over algorithmic cleverness
- Communication and collaboration over speed
- Java/JVM proficiency and OOP patterns
- Understanding of concurrency and real-world engineering concerns

The difficulty comes from:
- Writing production-quality code under observation
- Demonstrating strong OOP and design pattern knowledge
- Thinking about edge cases, error handling, testability
- Financial domain awareness in system design
- Product thinking integrated with engineering decisions

---

## 5. Topics That Come Up Frequently

### Coding
- **Data structures**: Array, Stack/Queue, HashSet/HashMap, Tree/Binary Tree, Heap, Graph
- **Complexity analysis**: time and space for all operations
- **Concurrency**: ConcurrentHashMap, thread safety, race conditions
- **Java specifics**: generics, streams, exceptions, memory management, collections framework
- **OOP**: SOLID principles, design patterns (especially circuit breaker, strategy)
- **Clean code**: DRY, KISS, single responsibility, testability
- **Practical problems**: interval merging, currency conversion, rate limiting, circuit breakers
- **Algorithms**: sorting, divide-and-conquer, dynamic programming, graph traversal

### System Design
- **Financial systems**: money transfers, ledgers, double-entry bookkeeping
- **Data consistency**: ACID transactions, idempotency, eventual consistency
- **Distributed systems**: microservices communication, Kafka, event-driven architecture
- **Scalability**: horizontal scaling, partitioning, async processing
- **Security**: encryption (TLS, AES/RSA), OAuth 2.0, JWT, RBAC, rate limiting
- **Compliance**: audit logs, immutable records, KYC/AML, GDPR, PCI DSS
- **Reliability**: multi-region replication, disaster recovery, circuit breakers
- **Monitoring**: observability, alerting, error handling strategies

### Product Mindset
- Customer problem identification
- Feature prioritization frameworks
- Measuring product success with data
- Balancing new features vs. tech debt
- Understanding Wise's mission and customer pain points
- Iterative product development

### Behavioral / Culture
- How you make decisions (data-driven)
- Collaboration and teamwork examples
- Handling disagreements without drama ("No drama. Good karma")
- Ownership mentality (you own your service from ideation to production)
- Transparency and customer obsession
- Why Wise? (demonstrate personal connection to the mission)

---

## 6. Wise Tech Stack (2025)

Understanding Wise's stack helps in both coding and system design interviews.

| Technology | Use Case |
|-----------|----------|
| **Java** | Primary backend language (~600+ services) |
| **Kotlin** | Some backend services (growing adoption) |
| **Spring Boot** | Microservice framework |
| **Kafka** | Async messaging, event streaming, log collection |
| **PostgreSQL** | Primary relational database |
| **Gradle** | Build system |
| **Kubernetes** | Container orchestration |
| **Go, Python, NodeJS** | Used in some services |
| **Trino** | Distributed SQL query engine |
| **Snowflake** | Data warehouse |
| **In-house chassis framework** | Standardized microservice creation (security, observability, DB, Kafka) |
| **In-house Gradle plugins** | Standardized build pipelines |

### Architecture Principles
- **1000+ microservices** in production
- **Microservice chassis**: in-house framework with standard defaults for security, observability, DB communication, Kafka
- **Automation at scale**: language-agnostic automation service for codebase-wide changes
- **Automated dependency upgrades** for Java services
- **Rack-aware Kafka replicas** for fault tolerance

---

## 7. System Design Expectations for Staff Level

### Interview Format (90 minutes)
1. Clarify functional requirements and constraints
2. Identify risks and edge cases
3. Propose high-level architecture
4. Deep-dive into core components
5. Discuss data consistency models
6. Explore scaling and resilience strategies
7. Analyze trade-offs

### Five Evaluation Areas
1. **Architectural Reasoning** -- Breaking problems into modular, well-defined components with clean boundaries
2. **Data Consistency Awareness** -- ACID transactions, idempotency, eventual consistency (critical for financial systems)
3. **Trade-off Thinking** -- Clearly articulating why you chose X over Y given constraints
4. **Simplicity and Maintainability** -- Wise's culture strongly values simplicity; avoid over-engineering
5. **Ownership and Clarity** -- Confidently explain trade-offs, suggest evolutionary paths as systems scale

### Common System Design Topics at Wise

#### Topic 1: Global Money Transfer System
- Design a system like Wise for cross-border money transfers
- Components: API Gateway, Transfer Service, Ledger Service, Currency Conversion Service, Notification Service
- Focus: compliance, FX conversion, payout partner integration
- Key: idempotency keys, transaction logs, reconciliation

#### Topic 2: Internal Ledger Service
- Double-entry bookkeeping with ACID guarantees
- Data replication, event sourcing for multi-currency updates
- Append-only databases for audit trails

#### Topic 3: Currency Conversion / Exchange Rate Service
- Rate ingestion from multiple providers
- Caching strategies with consistency guarantees
- Latency reduction, fallback mechanisms
- Handling stale rates

#### Topic 4: Fraud Detection Pipeline
- Layered real-time and offline risk evaluation
- Stream processing, append-only databases for compliance
- ML integration for anomaly detection

#### Topic 5: Transaction Notification System
- Event-driven design with idempotency
- Retry logic, delivery guarantees
- Multi-channel (email, push, SMS)

### Critical Design Principles for Wise
- **Consistency over availability** for core transactions (acceptable to delay rather than risk data errors)
- **Eventual consistency** for non-critical components (notifications, analytics)
- **Immutable audit logs** for traceability
- **Event sourcing** for transaction reconstruction
- **Secure-by-default** patterns and fail-safe mechanisms
- **Multi-region replication** for disaster recovery
- **Simple, evolutionary architecture** -- start simple, iterate

### Recommended Approach
1. Start with clarifying questions about scope and constraints
2. Begin with a simple solution, then iterate improvements
3. Articulate trade-offs explicitly at every decision point
4. Show awareness of financial domain requirements (compliance, auditability, correctness)
5. Connect technical decisions to user/business outcomes (trust, speed, compliance)
6. Think about testing, monitoring, and error handling strategies

---

## 8. What They Look For in Staff Candidates

### Wise Engineering Career Levels
| Level | Title | Scope |
|-------|-------|-------|
| IC1 | Junior Engineer | Small, well-defined tasks with team support |
| IC2 | Engineer | Independent execution, medium-sized projects |
| IC3 | Senior Engineer | Domain expert, technical roadmap ownership, mentoring |
| IC4 | Senior Engineer+ | Deep expertise, owns large impactful projects, drives technical + product roadmaps |
| **IC5** | **Staff Engineer** | **Multi-domain expert, leads solutions to biggest problems across squads** |
| IC6 | Principal Engineer | Company-wide strategy, shapes engineering standards |
| EL1 | Engineering Lead 1 | Owns 1 team domain, manages delivery + people (min IC3 expertise) |
| EL2 | Engineering Lead 2 | Owns 1+ teams, cross-functional leader (min IC4 expertise) |

### Staff Engineer (IC4) Expectations
- **Consistently own large-sized impactful projects**
- **Drive both technical AND product roadmaps** -- not just technical execution
- Deep expertise in your domain
- Expected to evaluate whether features are worth building (product judgment)
- Strong communication and prioritization skills
- Ability to unblock yourself and your team
- Proactively seek out difficult problems
- Deliver sustainable solutions (not just fast ones)

### What Sets Staff Apart from Senior at Wise
1. **Scope**: Senior owns technical roadmap for their team; Staff drives roadmaps across teams
2. **Product judgment**: Staff is expected to influence WHAT gets built, not just HOW
3. **Autonomy**: Staff is expected to own services end-to-end (ideation to production, including testing, performance, scaling, and production fixes)
4. **Impact**: Consistently leading large, impactful projects vs. contributing to them
5. **Mentoring**: Active mentoring and raising the bar for the team

### Compensation (UK, approximate)
| Level | Base Salary (GBP/year) | Notes |
|-------|----------------------|-------|
| IC1 | 47,000-65,000 | |
| IC2 | ~65,000-85,000 | |
| IC3 (Senior) | ~85,000-105,000 | |
| IC4 (Staff) | 105,000-130,000 | + equity (no cash bonus) |
| EL1 (Eng Lead) | 100,000-125,000 | |

- Equity awarded on top of base salary; no cash bonuses
- US positions command higher salaries reflecting local market

---

## 9. Tips and Patterns from Candidates

### General Tips
1. **Wise is NOT a LeetCode company** -- don't over-index on algorithm grinding
2. **Product mindset is essential** -- understand WHY you're building something, not just HOW
3. **Communication is heavily weighted** -- think aloud, explain trade-offs, ask questions
4. **Java proficiency helps significantly** -- most interviewers are Java engineers
5. **Know Wise's mission deeply** -- "Money without borders"; understand their fee model, how transfers work
6. **Start simple, iterate** -- both in coding and system design
7. **Treat the interviewer as a collaborator** -- pair programming means working together

### Coding Interview Tips
- Ask clarifying questions before coding
- Explain your thought process continuously
- Write clean, readable code with good naming
- Consider edge cases and error handling
- Discuss time/space complexity
- If stuck, talk through your thought process -- the interviewer can help
- Know Java concurrency basics (ConcurrentHashMap, thread safety)
- Practice SOLID principles and design patterns

### System Design Tips
- Start with requirements clarification (functional + non-functional)
- Always discuss data consistency for financial systems
- Mention idempotency for any write operation
- Think about compliance and audit trails
- Discuss monitoring and error handling
- Keep designs simple -- Wise values pragmatism over cleverness
- Connect your design to business outcomes (user trust, regulatory compliance)

### Product Interview Tips
- Read about Wise's products (multi-currency account, business account, Wise Platform)
- Think about metrics for success (what would you measure?)
- Have a framework for prioritization
- Show you can think from the customer's perspective
- No "right" answers -- they want structured, data-backed reasoning

### Red Flags (What Gets Candidates Rejected)
- Over-engineering solutions (complexity where simplicity works)
- Not explaining trade-offs
- Poor collaboration during pair programming
- No questions about the role, team, or product
- Lack of product awareness (treating engineering as just writing code)
- Cultural misalignment (ego-driven, drama-prone, not customer-focused)

---

## 10. Preparation Recommendations for Staff SWE

### Coding Prep (Medium Priority)
- **50-70 LeetCode Easy-Medium problems** focusing on practical patterns
- Focus on: HashMap, intervals, arrays, strings, basic graph traversal
- Practice writing **clean Java/Python code** with good OOP structure
- Implement common patterns: circuit breaker, rate limiter, currency converter
- Practice concurrency: thread-safe collections, basic synchronization
- Practice pair programming style: explain everything, ask for input
- Time yourself: 45-50 minutes per problem (simulating interview pace)

### System Design Prep (HIGH Priority)
- **Study Wise's engineering blog** (medium.com/wise-engineering) for actual architecture
- Practice designing: money transfer system, ledger service, exchange rate service
- Know Kafka deeply (partitioning, consumer groups, exactly-once, idempotency)
- Understand double-entry bookkeeping for financial systems
- Practice the structured approach: requirements -> architecture -> deep dive -> trade-offs -> scaling
- Study: event sourcing, CQRS, idempotency patterns, distributed transactions
- Know PostgreSQL (Wise's primary DB) trade-offs well
- Resources: "Grokking the System Design Interview", SystemDesignHandbook.com

### Product Thinking Prep (Medium-High Priority)
- Study Wise's products: personal transfers, multi-currency account, Wise Business, Wise Platform (API)
- Understand their fee model and how they make money
- Think about: how would you measure feature success? How would you prioritize?
- Read Wise's blog and press releases for recent product launches
- Prepare examples of when you influenced product decisions in past roles

### Cultural Prep (Medium Priority)
- Prepare STAR-format examples for:
  - Cross-team collaboration
  - Ownership of end-to-end systems
  - Making data-driven decisions
  - Handling disagreements constructively
  - Customer-focused problem solving
- Research Wise's values: transparency, customer obsession, ownership, "no drama good karma"
- Prepare a genuine answer for "Why Wise?" (personal connection to mission)

### Domain Knowledge (Helpful)
- Basic understanding of: FX rates, compliance (KYC/AML), payment rails (SWIFT, SEPA)
- How international money transfers work at a high level
- Why traditional banks are expensive for cross-border transfers
- Basic understanding of financial regulations (GDPR, PCI DSS)

---

## 11. Hello Interview - Reported Questions (Feb 2026)

### System Design (2 reports)

| Question | Level | Core Theme | Key Patterns |
|----------|-------|------------|--------------|
| **Merchant Payout System** | Staff | 10K TPS payments → periodic merchant payouts | Append-only ledger (double-entry), Kafka ingestion, idempotency keys, saga-based payouts, periodic snapshots, reconciliation |
| **Job Scheduler** | Senior | 10K jobs/sec, cron + ad-hoc, retry, history | Partitioned scheduling, Redis sorted sets, DynamoDB, heartbeats/leases, backpressure |

### Behavioral (1 report)

| Question | Level | Type |
|----------|-------|------|
| **"What project are you most proud of?"** | Senior | Behavioral → Use H1 (0→21 team, global platform) |

### Pattern Analysis — What Wise Actually Tests

**Dominant themes:**
1. **Financial correctness** — ledger, double-entry, idempotency, audit trail (core Wise DNA)
2. **Append-only/immutable data** — no mutable balance rows, snapshot + event log
3. **Saga pattern for payouts** — idempotent steps, compensation for failures
4. **High-throughput ingestion** — Kafka buffering, stateless frontends, dedup

**Key insight for pair programming:** The Merchant Payout is SD, but the financial patterns (idempotency, event processing, state machines) could appear as coding problems too. Practice implementing:
- Idempotency key checking
- Event processing with state tracking
- Simple ledger/balance calculation from events

**Alignment with research:** Merchant Payout = Wise's actual business. This is the most likely SD topic.

### Pair Programming — Confirmed Problems from Forums (Reddit, Blind, Glassdoor, JoinTaro)

| Problem | Description | Difficulty | Source |
|---------|-------------|------------|--------|
| **Circuit Breaker** | Implement in `WebClient.execute(Request)`: 3 fails in 10 min → stop 5 min | Medium | Glassdoor/JoinTaro Dec 2024 (got offer) |
| **Currency Converter/Exchange** | Send/receive money, refactor for edge cases | Easy-Medium | Glassdoor 2024-2025 |
| **Simple Cache** | Implement a cache | Easy-Medium | Glassdoor 2024 |
| **Rate Limiter** | Design + implement, concurrency | Medium | Blind 2024 |
| **Sorting Two Lists of Intervals** | Merge/sort interval lists | Medium | Blind/Glassdoor |
| **Code Refactoring** | Given existing code → "How would you improve this?" | Medium | JoinTaro Oct 2025 |
| **Integer to Roman** | Classic conversion | Easy-Medium | Glassdoor |
| **Find Pairs** | Finding pairs in array | Easy | Glassdoor |
| **Currency Exchange Service** | Exchange service + resiliency, cost, performance | Medium | Glassdoor 2024-2025 |

### ⚠️ Key Insights from Forums

1. **Refactoring variant exists** (Oct 2025): You receive existing code and improve it. Not always from-scratch.
2. **Speed matters**: Oct 2025 rejected candidate said "tasks weren't difficult, but I was working more slowly than I'd hoped."
3. **11% pass rate** for SE in London (JoinTaro, 27 data points) — extremely selective.
4. **Requirements change mid-problem**: They give base problem, then alter requirements to see how you adapt.
5. **Java is default** — MUST confirm with recruiter if Python is ok. Interviewers are Java engineers.

---

## 12. Key Sources & Links

### Official Wise Resources
- [Wise Interviews Overview](https://wise.jobs/step-2-interview)
- [Backend Pair Programming Interviews](https://wise.jobs/pair-programming-interviews)
- [System Design Interviews](https://wise.jobs/system-design-interviews)
- [Engineering Career Map](https://wise.jobs/engineering-career-map)
- [Wise Tech Stack 2025](https://medium.com/wise-engineering/wise-tech-stack-2025-update-d0e63fe718c7)
- [Pair Programming at Wise (blog)](https://www.wise.jobs/2020/10/13/pair-programming-interviews-at-transferwise/)

### Candidate Experience Reports
- [Glassdoor: Wise Software Engineer Interviews](https://www.glassdoor.com/Interview/Wise-Software-Engineer-Interview-Questions-EI_IE637715.0,4_KO5,22.htm)
- [Glassdoor: Wise Senior SWE Interviews](https://www.glassdoor.com/Interview/Wise-Senior-Software-Engineer-Interview-Questions-EI_IE637715.0,4_KO5,29.htm)
- [Blind: Pair Programming Interview](https://www.teamblind.com/post/wisetransferwise-1st-pair-programming-interview-z31lddtc)
- [Blind: Senior Backend Interviews](https://www.teamblind.com/post/Wise-Transferwise-Senior-Backend-Interviews-eVHTQLPt)
- [Blind: System Design Interview](https://www.teamblind.com/post/Wise---System-design-interview-T1ZPPgWt)
- [LeetCode: Wise Estonia Offer Experience](https://leetcode.com/discuss/interview-experience/1597982/paypay-japan-wise-transfer-wise-estonia-offer/)
- [InterviewQuery: TransferWise SWE Guide](https://www.interviewquery.com/interview-guides/transferwise-software-engineer)

### Preparation Resources
- [Wise System Design - Educative](https://www.educative.io/blog/wise-system-design-interview)
- [Wise System Design - SystemDesignHandbook](https://www.systemdesignhandbook.com/guides/wise-system-design-interview/)
- [Prepfully: Wise Interview Questions 2026](https://prepfully.com/interview-questions/wise)
- [Levels.fyi: Wise Compensation](https://www.levels.fyi/companies/wise/salaries/software-engineer)
- [Pragmatic Engineer: Senior SWE at Wise](https://blog.pragmaticengineer.com/what-is-a-senior-software-engineer-at-wise-and-amazon/)
- [Behavioral Questions Template](https://nerohoop.gitbooks.io/behavioral-questions/transferwise.html)

### Engineering Blog (for domain knowledge)
- [Wise Engineering on Medium](https://medium.com/wise-engineering)
- [GitHub: transferwise/interview (archived)](https://github.com/transferwise/interview)
