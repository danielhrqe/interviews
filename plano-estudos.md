# Plano de Estudos - Fev/Mar 2026

> **Atualizado: 23/fev/2026** — Plano definitivo com Hello Interview data + fóruns + metodologia hands-on
> **Estilo de aprendizagem:** Aprende fazendo, escrevendo e desenhando. Mínimo de leitura passiva.

---

## Visão Geral

| Período | Foco | Entrevista |
|---------|------|------------|
| 23-26 fev | DoorDash (System Design + Leadership) | **Qui 26/fev 15h** |
| 24-27 fev | Wise (Pair Programming prep) | **Sex 27/fev 11h BRT** |
| 28 fev - 1 mar | QuintoAndar SD/ML | **2/mar 12h** |
| 2-3 mar | Nubank Architecture | **4/mar 10h** |
| 4-8 mar | QuintoAndar Coding | **9/mar 10h** |

---

## Metodologia: Learn by Doing

> Você NÃO vai só ler. Cada bloco tem uma entrega concreta.

| Método | Como funciona | Exemplo |
|--------|--------------|---------|
| **DESENHAR** | Diagrama à mão/draw.io de cada sistema. Sem copiar — do zero, de memória. | Desenhar Food Reviews: client → API → Kafka → ... |
| **ESCREVER** | Resumo em 5 bullet points com suas palavras depois de cada leitura. Sem colar. | "Saga = cada step idempotent, se falhar → compensation" |
| **CODIFICAR** | Implementar padrões em Python. Não ler sobre — FAZER. | Implementar circuit breaker com classes em Python |
| **FALAR** | Explicar em voz alta em inglês como se fosse a entrevista. Gravar se possível. | "I would use Redis sorted sets because..." |
| **QUIZ** | Comigo, sem consulta, em inglês. Erro = gap identificado. | "What happens if the payment processor times out?" |

---

## Progresso até agora (19-23/fev)

### Feito
- [x] 6 histórias STAR montadas
- [x] Mock leadership #1 (borderline) + #2 (Hire, borderline Strong Hire)
- [x] Pesquisa cross-company system design
- [x] Hello Interview: How to Prepare, Core Concepts, Key Technologies, Patterns
- [x] Hello Interview: **Local Delivery Service** (Easy)
- [x] Hello Interview: **Uber** (Hard)
- [x] Hello Interview: **Rate Limiter** (Medium)
- [x] Review/recall + prática no Hello Interview (23/fev manhã)
- [x] Google HR Chat (23/fev 11h)
- [x] Research completo: Hello Interview reports + Reddit/Blind/Glassdoor

### Pendente (incorporado no plano abaixo)
- [ ] Hello Interview: **Job Scheduler** (Hard)
- [ ] Hello Interview Patterns: Dealing with Contention, Multi-step Processes, Real-time Updates
- [ ] Hello Interview Technologies: Kafka, Redis, Elasticsearch
- [ ] Mock System Design #1 e #2
- [ ] Leadership em voz alta + STAR stories cronometradas
- [ ] Wise: implementar problemas em Python (circuit breaker, intervals)

---

## ⚠️ O que REALMENTE cai (dados de 100+ reports)

### DoorDash SD — Top Questions

| # | Question | Reports | Temas-chave |
|---|----------|---------|-------------|
| 1 | **Food Reviews + Payouts** | **37** | Sharded counters, Elasticsearch, saga payouts, fraud |
| 2 | **Donations Website** | **26** | Idempotency, circuit breaker, failover PSP, live counters |
| 3 | **Job Scheduler** | **11** | Redis sorted sets, partitioning, leases, backpressure |
| 4 | **Review + Rewards** | **11** | Variação do #1 |
| 5 | **Instagram** | **10** | Fan-out feeds, media upload |

**Tema transversal:** Payments/idempotency/saga aparece em TUDO.

### Wise Pair Programming — Problems Confirmed

| Problem | Difficulty | Estilo |
|---------|-----------|--------|
| Circuit Breaker | Medium | OOP, state management |
| Currency Converter | Easy-Medium | Clean code, edge cases |
| Rate Limiter | Medium | HashMap, time-based |
| Intervals (merge/sort) | Medium | Arrays, sorting |
| Code Refactoring | Medium | Recebe código → melhora |

**Tema transversal:** Clean code + OOP > algoritmos. Velocidade importa. Requirements mudam mid-problem.

---

## SEG 23/FEV — 14:00-18:30 (4.5h)

### BLOCO 1: Quiz Recall (14:00-14:30) — 30 min
**Método: FALAR (em inglês, comigo, sem consulta)**

Quiz sobre o que você já leu:
- Framework 7 steps de SD (listar de memória)
- Napkin math: QPS de 1M req/day? Storage de 1KB × 1B?
- Uber: como funciona matching? Que DB para locations?
- Rate Limiter: sliding window vs token bucket? Onde fica?
- Delivery Service: state machine de um pedido?

> **Entrega:** Score + lista de gaps

---

### BLOCO 2: Hello Interview — Contention + Multi-step + Kafka (14:30-16:00) — 1.5h
**Método: LER → ESCREVER → DESENHAR**

**14:30-15:00 — Ler no Hello Interview (30 min):**
- [ ] Pattern: **Dealing with Contention** (~10 min)
- [ ] Pattern: **Multi-step Processes** (~10 min)
- [ ] Technology: **Kafka** (~10 min)

**15:00-15:20 — Escrever resumos (20 min):**
Depois de cada leitura, fechar a aba e escrever de memória:
- [ ] Contention: 5 bullet points (o que é, quando acontece, como resolver)
- [ ] Multi-step/Saga: 5 bullet points (por que, idempotency, compensation)
- [ ] Kafka: 5 bullet points (quando usar, partitions, consumer groups, guarantees)

**15:20-16:00 — Desenhar Food Reviews system (40 min):**
Com base no que leu + breakdown que você tem, desenhar do zero (draw.io ou papel):
- [ ] Diagrama completo do Food Reviews + Payouts
- [ ] Marcar onde entra Kafka, Redis, Elasticsearch
- [ ] Marcar onde está o saga pattern para payouts
- [ ] Marcar onde estão os sharded counters
- [ ] Anotar: que pergunta o entrevistador faria aqui? (deep dive points)

> **Entrega:** 3 resumos escritos + 1 diagrama desenhado do zero

---

### BLOCO 3: Mock System Design #1 comigo (16:00-17:30) — 1.5h
**Método: FALAR + DESENHAR (simulação real)**

- [ ] 60 min de mock com timer — eu sou o entrevistador DoorDash
  - Problema: **Food Reviews + Payouts** OU **Donations Website**
  - Você desenha no draw.io/papel enquanto fala
  - Eu interrompo, faço deep dive, peço trade-offs (como DoorDash faz)
- [ ] 30 min feedback:
  - O que faltou?
  - Onde hesitou?
  - O que o entrevistador pediria mais detalhes?
  - Score 1-10

> **Entrega:** Design completo + feedback escrito + gaps identificados

---

### BLOCO 4: Leadership em voz alta (17:30-18:30) — 1h
**Método: FALAR (em inglês, cronometrado)**

**17:30-18:00 — STAR stories (30 min):**
- [ ] H1 (Team building 0→21) — falar em voz alta, cronometrar. MAX 3 min.
- [ ] H3 (Firing) — falar em voz alta, cronometrar. MAX 2.5 min.
- [ ] H5 (Diversity) — falar em voz alta, cronometrar. MAX 2 min.
- Se qualquer uma passar do tempo: cortar, renarrar mais curta.

**18:00-18:30 — Respostas rápidas (30 min):**
- [ ] "Ignore the underperformer" — falar em voz alta, max 1 min
- [ ] "Why DoorDash?" — falar em voz alta, max 1 min
- [ ] "Tell me about a conflict" — H6, falar em voz alta, max 2.5 min

> **Entrega:** Cada história cronometrada. Anotar: qual ficou longa? Qual ficou confusa?

---

### REVIEW noite (15 min)
- [ ] Escrever 3 bullet points: aprendi / errei / revisar amanhã
- [ ] Olhar gaps do mock → o que estudar terça

---

## TER 24/FEV — Dia intenso (DoorDash final + Wise início)

### RECALL (9:00-9:30) — 30 min
**Método: QUIZ comigo, sem consulta, em inglês**

- Redesenhar de memória o diagrama de Food Reviews (em 5 min, no papel)
- Quiz: idempotency key — o que é? Onde coloca? O que acontece sem?
- Quiz: saga pattern — 3 steps de um payout, como compensa falha?
- Quiz: gaps do mock de ontem (o que faltou?)

> **Entrega:** Score + diagrama de memória

---

### ABSORVER + DESENHAR (9:30-11:30) — 2h
**Método: LER → ESCREVER → DESENHAR**

**9:30-10:00 — Hello Interview: Job Scheduler breakdown (30 min)**
- [ ] Ler o breakdown completo
- [ ] Fechar e escrever 5 bullet points de memória

**10:00-10:30 — Hello Interview: Redis + Real-time Updates (30 min)**
- [ ] Ler Technology: **Redis** (~15 min)
- [ ] Ler Pattern: **Real-time Updates** (~15 min)
- [ ] Escrever: quando Redis vs Kafka? Quando WebSocket vs SSE vs polling?

**10:30-11:00 — Desenhar Donations Website do zero (30 min)**
- [ ] Diagrama completo sem consultar nada
- [ ] Marcar: idempotency keys, state machine, failover PSP, live counters
- [ ] Comparar com o breakdown → o que faltou?

**11:00-11:30 — Hello Interview: Elasticsearch (30 min)**
- [ ] Ler Technology: **Elasticsearch** (~15 min)
- [ ] Escrever: quando usar ES vs SQL? Inverted index = o quê?
- [ ] Anotar: como ES se encaixa no Food Reviews?

> **Entrega:** Job Scheduler resumo + Donations diagrama + tech summaries

---

### APLICAR: Mock SD #2 (13:30-15:00) — 1.5h
**Método: FALAR + DESENHAR (simulação real)**

- [ ] 60 min mock com timer — problema DIFERENTE do #1
  - Se ontem foi Food Reviews → hoje Donations Website (ou vice-versa)
  - Se sobrar confiança: Job Scheduler
- [ ] 30 min feedback: comparar com mock #1. Melhorou onde?

> **Entrega:** Design #2 completo + comparação com #1

---

### APLICAR: Mock Leadership #3 (15:00-16:00) — 1h
**Método: FALAR (simulação completa em inglês)**

- [ ] 45 min mock: eu sou o entrevistador DoorDash, Team Building & Hiring
  - Vou cobrir: team building, underperformer, coaching, diversity, conflict
  - Vou interromper e pedir follow-ups como entrevistador real
- [ ] 15 min feedback: score 1-10, gaps, o que melhorar

> **Entrega:** Score + 3 melhorias específicas

---

### WISE PREP: Coding hands-on (16:30-18:30) — 2h
**Método: CODIFICAR (Python, OOP, pair programming style)**

**16:30-17:00 — Hello Interview Coding: Intervals Overview (30 min)**
- [ ] Ler HI Coding: **Intervals Overview** (conceito)
- [ ] Resolver: **Merge Intervals** no Hello Interview (praticar)

**17:00-18:00 — Implementar Circuit Breaker em Python (1h)**
- [ ] Implementar do zero, sem consultar:
  - Classe `CircuitBreaker` com states: CLOSED, OPEN, HALF_OPEN
  - Config: failure_threshold, timeout, recovery_timeout
  - Método `execute(request)` que monitora falhas
  - Transições de estado automáticas
- [ ] Escrever pelo menos 3 test cases
- [ ] Refatorar: aplicar SOLID, renomear, limpar
- [ ] Praticar: explicar o código em voz alta em inglês enquanto escreve

**18:00-18:30 — Implementar Rate Limiter simplificado (30 min)**
- [ ] Sliding window rate limiter em Python
- [ ] Pensar em voz alta enquanto codifica
- [ ] Discutir: O(1) vs O(n)? Thread-safe? Como testar?

> **Entrega:** 2 implementações Python (circuit breaker + rate limiter) + testes

---

### REVIEW noite (15 min)
- [ ] 3 bullet points: aprendi / errei / revisar
- [ ] Comparar mock #1 vs #2: onde melhorou?
- [ ] Quão confiante estou para DoorDash? (1-10)

---

## QUA 25/FEV — Descanso ativo + Wise polish

### MANHÃ: DoorDash revisão final (9:00-10:00) — 1h max
**Método: DESENHAR + FALAR (tudo de memória)**

**9:00-9:20 — Desenhar 2 diagramas de memória (20 min)**
- [ ] Food Reviews + Payouts — diagrama completo, sem consulta, 10 min
- [ ] Donations Website — diagrama completo, sem consulta, 10 min
- Comparar com seus diagramas de seg/ter. Se lembrou de tudo → pronto.

**9:20-9:40 — Falar respostas de memória (20 min)**
- [ ] 5 números-chave — dizer em voz alta sem olhar
- [ ] "Why DoorDash?" — 1 min sem parar
- [ ] "Ignore underperformer" — 1 min sem parar
- [ ] H1 resumida — 2 min sem parar

**9:40-10:00 — Checklist final DoorDash (20 min)**
- [ ] Revisar MASTER-PREP: checklist respostas (só olhar, já sabe)
- [ ] Revisar napkin math (só olhar)
- [ ] Anotar 3 coisas que quer lembrar na hora (cola mental)

> **Entrega:** 2 diagramas de memória + checklist mental pronto

---

### TARDE: Wise pair programming prep (14:00-16:00) — 2h
**Método: CODIFICAR (pair programming simulation comigo)**

**14:00-15:00 — Mock pair programming comigo (1h)**
- [ ] Eu dou um problema estilo Wise (não vou dizer qual antes)
- [ ] Você codifica em Python no seu editor
- [ ] Pensa em voz alta em inglês O TEMPO TODO
- [ ] Eu faço perguntas como interviewer: "Why did you choose this?" "What about edge case X?"
- [ ] Eu mudo os requirements no meio (como Wise faz!)
- [ ] 45 min coding + 15 min feedback

**15:00-15:30 — Hello Interview Coding: Stack Overview + Valid Parentheses (30 min)**
- [ ] Ler Overview de Stack (~5 min)
- [ ] Resolver Valid Parentheses no HI
- [ ] Relevante: Wise pede problemas práticos, stack é padrão

**15:30-16:00 — Hello Interview Coding: Two Pointers Overview (30 min)**
- [ ] Ler Overview (~5 min)
- [ ] Resolver Move Zeroes ou Container With Most Water no HI
- [ ] Estes padrões aparecem em problemas de intervals/arrays da Wise

> **Entrega:** 1 mock pair programming completo + 2 problemas resolvidos

---

### SETUP (16:00-16:30)
- [ ] Testar câmera, mic, internet
- [ ] Abrir HackerRank CodePair — navegar, entender interface
- [ ] Preparar ambiente: sala quieta, água, celular silenciado
- [ ] Testar setup para DoorDash (HackerRank whiteboard + Zoom)

### NOITE
- [ ] Descansar. Nada de estudo novo.
- [ ] Se quiser: ouvir um podcast leve ou assistir algo relaxante
- [ ] Dormir cedo (23h no máximo)

---

## QUI 26/FEV — DIA DA ENTREVISTA DOORDASH 🎯

### Manhã (30 min, 9:00-9:30)
**Método: OLHAR (não estudar)**
- [ ] Olhar diagrama de Food Reviews (que você desenhou)
- [ ] Olhar diagrama de Donations (que você desenhou)
- [ ] 5 números (dizer em voz alta 1x)
- [ ] Framework 7 steps (olhar 1x)
- [ ] ⚠️ ZERO conteúdo novo. Confiança > conhecimento neste ponto.

### Almoço tranquilo (12:00-13:30)
- Comida leve, hidratação, banho
- Se ansioso: respiração 4-7-8 (inspirar 4s, segurar 7s, expirar 8s)

### Preparação final (14:00-14:45)
- [ ] Setup técnico testado (câmera, mic, HackerRank, Zoom)
- [ ] Água, caderno, caneta na mesa
- [ ] Reler cola mental (3 coisas que anotou quarta)
- [ ] Entrar na call 5 min antes

### 15:00 — DOORDASH ROUND 1
- **System Design (60 min):** problema hipotético. Use framework 7 steps.
- **Team Building & Hiring (45 min):** STAR stories. "I did", números, max 3 min cada.

### Pós-entrevista (17:00-17:30)
- [ ] Anotar imediatamente: o que caiu, o que foi bem, o que foi mal
- [ ] Respirar. Não julgar. Está feito.

### Noite: Wise final warmup (19:00-20:00) — 1h
**Método: FALAR + CODIFICAR (leve)**
- [ ] Reler SOLID principles — 1 frase cada (5 min)
- [ ] Resolver 1 problema Python simples pensando em voz alta (20 min)
- [ ] Reler problemas confirmados Wise: circuit breaker, rate limiter, currency converter, intervals, refactoring (10 min)
- [ ] Pair programming self-talk: "I'm going to start with... because..." — praticar 15 min
- [ ] Dormir cedo

---

## SEX 27/FEV — DIA DA ENTREVISTA WISE 🎯

### Manhã (30 min, 9:30-10:00)
**Método: OLHAR + FALAR**
- [ ] SOLID: Single Responsibility, Open/Closed, Liskov, Interface Segregation, Dependency Inversion
- [ ] Falar em voz alta: "Start simple, iterate. Explain everything. Ask the interviewer."
- [ ] Lembrete: colaboração > velocidade. Perguntar > assumir.
- [ ] ⚠️ ZERO conteúdo novo.

### Setup (10:00-10:45)
- [ ] HackerRank CodePair aberto e testado
- [ ] Python environment pronto
- [ ] `from collections import Counter, defaultdict, deque` — ter na cabeça
- [ ] Água, sala quieta, celular silenciado
- [ ] Entrar 5 min antes

### 11:00 BRT — WISE PAIR PROGRAMMING
- 60 min, Python, HackerRank CodePair
- Lembrar: pensar em voz alta, perguntar, colaborar, start simple → iterate

### Pós-entrevista (12:00-12:30)
- [ ] Anotar: o que caiu, como foi, o que melhorar
- [ ] Debrief DoorDash + Wise juntos

### Tarde: Transição para próxima fase
- [ ] Ler MASTER-PREP seção QuintoAndar SD/ML
- [ ] Descansar — semana foi intensa

---

## FASE 2: QuintoAndar SD/ML + Nubank (28 fev - 4 mar)

### Sáb 28/fev
**ABSORVER + ESCREVER (2h)**
- [ ] ML fundamentals: supervised vs unsupervised, bias-variance, overfitting/underfitting
- [ ] Deep Learning: Transformers, attention, embeddings
- [ ] Hello Interview: **Payment System** breakdown (prep Nubank)
- [ ] Escrever flashcards de cada conceito (pergunta → resposta, 1 frase)

**APLICAR (1-2h)**
- [ ] Quiz ML comigo (flashcards MASTER-PREP.md)

### Dom 1/mar (véspera QA SD/ML)
**RECALL (30 min)**
- [ ] Quiz ML + GenAI concepts sem consulta

**ABSORVER + DESENHAR (1-2h)**
- [ ] GenAI: LLMs, RAG, fine-tuning, prompt engineering
- [ ] MLOps: feature stores (Butterfree), model serving, monitoring, drift
- [ ] Desenhar: ML pipeline end-to-end (data → features → train → serve → monitor)

**APLICAR (1-2h)**
- [ ] **Mock QA SD/ML comigo** (case: ML platform ou RAG system)

### Seg 2/mar — DIA DA ENTREVISTA QA SD/ML
- [ ] Manhã: revisão leve conceitos ML + stack QA (30 min)
- [ ] **12h: QuintoAndar System Design/ML** (60min, Google Meet)
- [ ] Tarde: transição → Nubank Architecture
- [ ] Event-driven architecture (Kafka deep dive)
- [ ] Hexagonal Architecture (ports & adapters) — desenhar diagrama

### Ter 3/mar (véspera Nubank)
**RECALL (30 min)**
- [ ] Quiz Nubank: event-driven, hexagonal, Simple vs Easy

**ABSORVER + DESENHAR (1-2h)**
- [ ] "Simple vs Easy" do Nubank
- [ ] Imutabilidade + Datomic
- [ ] Desenhar: event feed system (Kafka → consumers → DB → API)

**APLICAR (1-2h)**
- [ ] **Mock Nubank Architecture comigo** (colaborativo, estilo Nubank)

### Qua 4/mar — DIA DA ENTREVISTA NUBANK
- [ ] Manhã: revisão leve (30 min)
- [ ] **10h: Nubank Architecture** (60min, colaborativo, Draw.io/Miro)
- [ ] Tarde: Debrief + transição coding

---

## FASE 3: QuintoAndar Coding + Google (4-13 mar)

### Metodologia Coding
**Cada dia = 1 pattern. Cada pattern segue:**
1. **Ler Overview** no Hello Interview (10 min)
2. **Resolver 2 problemas** no Hello Interview — escrever código, rodar (40 min)
3. **Review comigo**: Big O, edge cases, otimização (10 min)

### Hello Interview Coding — Plano por Dia

| Dia | Pattern | Problemas HI | Relevância |
|-----|---------|-------------|------------|
| Qua 4/mar tarde | HashMap + Two Pointers | Two Sum Sorted, Container Most Water, Move Zeroes | ALL companies |
| Qui 5/mar | Sliding Window + Intervals | Max Sum K, Longest Substring, Merge Intervals | QA Codility + Wise |
| Sex 6/mar | Stack + Binary Search | Valid Parentheses, Daily Temperatures, Koko Bananas | QA + Google |
| Sáb 7/mar | BFS + DFS | Level Order, Number of Islands, Rotting Oranges | Google + DoorDash |
| Dom 8/mar | Trees + Graphs | Max Depth, Validate BST, Course Schedule | Google |
| Seg 9/mar manhã | REVIEW: resolver 2 problemas fracos + cheatsheet | — | QA Codility |

### Seg 9/mar — DIA DA ENTREVISTA QA CODING
- [ ] **10h: QuintoAndar Coding** (60min, Codility)

### Pós QA: Google Prep (10-?? mar)
- [ ] DP: Decode Ways, Longest Increasing Subsequence, Job Scheduling
- [ ] Backtracking: Word Search, Subsets, Generate Parentheses
- [ ] Heap: Kth Largest, Merge K Sorted Lists
- [ ] Trie: Implement Trie, Prefix Matching
- [ ] Greedy: Best Time Buy/Sell Stock, Jump Game
- [ ] Prefix Sum: Subarray Sum Equals K

---

## Quick Reference

### 5 Números DoorDash
1. **0 → 21 pessoas** em 3 anos (8-11 diretos)
2. **600+ usuários** na plataforma global
3. **2M queries/day** + 70K daily executions
4. **$2M de economia** em otimização
5. **7+ promoções** patrocinadas + 15+ contratações

### Checklist respostas DoorDash
- [ ] "Team building" → H1 com contexto + números
- [ ] "Underperformer" → Dois exemplos (fire + depressão)
- [ ] "Someone you developed" → SRE → strategic → promoção
- [ ] "Diversity" → Pipeline + processo estruturado + 4/7 Black/Brown
- [ ] "Stakeholder conflict" → NA vs Global + RFC process
- [ ] "Ignore underperformer" → Não. Moral, carga, padrão do time
- [ ] "Why DoorDash?" → Marketplace 3 lados, escala, data/ML, ownership

### Hello Interview Breakdowns — Status
- [x] Local Delivery Service (Easy)
- [x] Uber (Hard)
- [x] Rate Limiter (Medium)
- [ ] **Job Scheduler** (Hard) ← ter 24/fev
- [ ] **Payment System** (Hard) ← sáb 28/fev (prep Nubank)

### Hello Interview Patterns — Status
- [ ] **Dealing with Contention** ← seg 23/fev
- [ ] **Multi-step Processes** ← seg 23/fev
- [ ] **Real-time Updates** ← ter 24/fev
- [ ] Scaling Reads ← quando sobrar tempo
- [ ] Scaling Writes ← quando sobrar tempo

### Hello Interview Technologies — Status
- [ ] **Kafka** ← seg 23/fev
- [ ] **Redis** ← ter 24/fev
- [ ] **Elasticsearch** ← ter 24/fev
- [ ] PostgreSQL ← quando sobrar tempo
- [ ] DynamoDB ← quando sobrar tempo
