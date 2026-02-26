# System Design — Study Notes (v2 — deep edition)

> **Updated:** 25/fev/2026
> Ler todo dia. Foco em COMO funciona mecanicamente, não só O QUE é.

---

## Índice

### 1. Ferramentas (Tools)
- [Kafka — Distributed Commit Log](#kafka--distributed-commit-log)
- [Redis — In-Memory Data Store](#redis--in-memory-data-store)
- [PostgreSQL](#postgresql)

### 2. Padrões de Design (Patterns)
- [Scaling Reads](#scaling-reads--novo)
- [Scaling Writes](#scaling-writes--novo)
- [Real-Time Updates](#real-time-updates--novo)
- [Multi-Step Process](#multi-step-process)
- [Contention](#contention) (Pessimistic Lock, OCC, Saga, 2PC)
  - [Saga Pattern + Pagamentos](#1-saga-pattern--muito-importante-para-sistemas-de-pagamento)
  - [Reconciliação](#reconciliação--a-rede-de-segurança-final)
- [Outbox Pattern](#outbox-pattern--aprendi-no-mock--fixando)
- [Async After 200](#async-after-200--aprendi-no-mock--fixando)
- [Token Bucket](#token-bucket--rate-limiting-algorithm)
- [CAP Theorem](#cap-theorem)

### 3. Problemas Praticados
- [Rate Limiter](#rate-limiter)
- [Uber / Ride Matching](#uber--ride-matching)
- [Food Reviews + Payouts](#food-reviews--payouts-mock-24fev--borderline-hire)
- [Job Scheduler](#job-scheduler)

### 4. Referência Rápida
- [Napkin Math](#4-napkin-math--referência-rápida)
- [Framework SD (7 passos)](#5-framework-sd-usar-em-toda-entrevista)
- [Decision Cards](#6-decision-cards)

---

# 1. Ferramentas (Tools)

## Kafka — Distributed Commit Log

**O que é:** plataforma de streaming de eventos. Diferente de uma fila tradicional (RabbitMQ/SQS), Kafka é um **LOG APPEND-ONLY** — mensagens não são deletadas após consumo. Isso permite replay, múltiplos consumers, e audit trail.

### Como funciona mecanicamente

**Producer publica mensagem:**
1. Producer envia `(key, value, timestamp, headers)` para um topic
2. Se key é null → round-robin entre partitions
   Se key existe → `hash(key) % num_partitions` → sempre mesma partition
3. Mensagem é APPEND ao final do log da partition (nunca modifica dados anteriores)
4. Broker retorna offset (posição no log) como confirmação

**Consumer lê mensagem:**
1. Consumer faz `poll()` pedindo mensagens a partir do seu último offset
2. Broker retorna batch de mensagens
3. Consumer processa e faz commit do offset (marca "li até aqui")
4. Se consumer cair e reiniciar, continua do último offset commitado

### Componentes
- **Brokers:** nós do cluster. Cada broker armazena partitions.
- **Topics:** agrupamento lógico (ex: "payments", "votes")
- **Partitions:** unidade de paralelismo. Cada partition = 1 log ordenado.
  > ⚠️ **IMPORTANTE:** ordering só é garantido DENTRO de uma partition, não entre partitions.
- **Consumer Groups:** grupo de consumers que dividem partitions entre si.
  - Regra: cada partition → exatamente 1 consumer do grupo.
  - Se 6 partitions e 3 consumers → cada consumer lê 2 partitions.
  - Se 6 partitions e 8 consumers → 2 consumers ficam idle (desperdício).

### Replication (eu esqueci isso)
- Cada partition tem N cópias (replication factor, ex: RF=3)
- 1 cópia é **LEADER** (recebe writes), outras são **FOLLOWERS** (replicam)
- Se leader cai, um follower é eleito novo leader (automático via ZooKeeper/KRaft)
- **ISR** (In-Sync Replicas): followers que estão up-to-date com o leader
- `acks=all`: producer espera todos ISR confirmarem → mais seguro, mais lento
- `acks=1`: producer espera só o leader → mais rápido, pode perder dados

### Delivery Semantics
| Modo | Como funciona | Risco |
|------|---------------|-------|
| at-most-once | Consumer commita offset ANTES de processar | Pode perder msg |
| **at-least-once (DEFAULT)** | Consumer commita DEPOIS de processar | Pode duplicar — precisa idempotência! |
| exactly-once | Transactional producers + idempotent consumers | Mais caro |

### Kafka como Fila vs Stream
- **Fila (queue):** 1 consumer group, cada msg processada por 1 consumer. Similar a SQS.
- **Stream:** múltiplos consumer groups, cada um lê todas as msgs independentemente.
  Ex: mesmo tópico "orders" é lido pelo PaymentService E pelo NotificationService.

### Números
| Métrica | Valor |
|---------|-------|
| Throughput | 1M+ msgs/sec (cluster) |
| Latência | 2-10ms (publicação), depende do acks |
| Retenção | Configurável (7 dias default, pode ser infinito) |

**Quando usar:** desacoplamento, event-driven, high throughput, precisa de replay/audit
**Quando NÃO usar:** request-response, <100 msgs/sec (overkill), precisa ordering global
**Pitch:** *"I'd use Kafka to decouple services with durable, ordered event delivery and the ability to replay events for recovery"*

---

## Redis — In-Memory Data Store

**O que é:** banco in-memory key-value com estruturas de dados ricas.
Single-threaded para commands → **TODA operação é atômica** por natureza.

### Como funciona mecanicamente

**Write (SET/INCR):**
1. Client envia comando (ex: `INCR review:123:votes`)
2. Redis processa em single thread (nenhum outro comando executa ao mesmo tempo)
3. Modifica o valor na memória RAM
4. Retorna resultado ao client
5. Se AOF habilitado, appenda o comando no arquivo de log em disco (async)

**Read (GET):**
1. Client envia comando (ex: `GET user:session:456`)
2. Redis busca na hash table interna — **O(1)**
3. Retorna valor — latência: **~microsegundos (sub-millisecond)**

### Estruturas de dados e quando usar cada uma

| Estrutura | O que é | Quando usar | Exemplo |
|-----------|---------|-------------|---------|
| **String** | Valor simples. INCR/DECR atômico | Counters, cache simples, rate limiting | `INCR review:123:votes` → retorna 457 |
| **Hash** | Objeto com campos | User profile, session data | `HSET user:123 name "João" age 30` |
| **List** | Lista ordenada. LPUSH/RPOP = FIFO | Filas simples, últimas atividades | `LPUSH notifications:user:123 "new_vote"` |
| **Set** | Conjunto de valores únicos | Tags, deduplicação | `SADD online_users "user:123"` |
| **Sorted Set (ZSet)** ⭐ | Set ordenado por SCORE | Leaderboards, top-N, rankings | `ZADD product:42:reviews 457 "review:123"` |
| **HyperLogLog** | Estimativa de contagem única (~12KB) | Unique visitors (~99% precisão) | `PFADD page_views:homepage "user:123"` |
| **Streams** | Log append-only (mini-Kafka) | Event sourcing simples | — |

> ⭐ **Sorted Set é o MAIS IMPORTANTE para entrevistas:**
> - `ZADD product:42:reviews 457 "review:123"` (score = 457 upvotes)
> - `ZREVRANGE product:42:reviews 0 9` (top 10 reviews)
> - Complexidade: O(log N) insert, O(log N + M) range query

### TTL e Eviction (EU ERREI ISSO — agora fixado)
- TTL **NÃO é automático**. Você seta: `EXPIRE key 3600` (1 hora)
- Sem EXPIRE, dado fica na memória **PARA SEMPRE**
- Quando memória enche, Redis aplica **EVICTION POLICY:**

| Policy | Comportamento |
|--------|---------------|
| noeviction | Retorna erro (default) |
| allkeys-lru | Remove keys menos recentemente usadas |
| volatile-lru | Remove keys COM TTL menos recentemente usadas |
| allkeys-random | Remove keys aleatórias |

> 💡 *"I'd set TTL on cache entries and use LRU eviction as a safety net when memory pressure increases"*

### Persistência (se Redis cair, como recuperar?)
| Modo | Como funciona | Trade-off |
|------|---------------|-----------|
| **RDB** (snapshot) | Foto da memória a cada X min | Rápido recovery, perde dados entre snapshots |
| **AOF** (append-only file) | Loga cada write em disco | Seguro (~1 sec perda max), recovery mais lento |
| **Híbrido** (RDB + AOF) | Melhor dos dois mundos | Recomendado para produção |

### Distributed Lock (como funciona mecanicamente)
```
1. Client A: SET lock:resource:123 "clientA" NX EX 30
   NX = só seta se key NÃO existe. EX 30 = expira em 30s.
2. Retornou OK → lock adquirido. Client A processa.
3. Retornou nil → outro client tem o lock. Espera ou retry.
4. Client A termina → DEL lock:resource:123 (libera o lock)
5. Se Client A crashar → lock expira em 30s automaticamente (TTL salva)
```
> ⚠️ **PROBLEMA:** em Redis Cluster, lock pode ser perdido durante failover.
> Solução: **Redlock** (lock em N/2+1 nodes), mas adiciona complexidade.

### Redis Cluster (como distribui dados)
- **16384 hash slots** divididos entre nodes
- Cada key: `CRC16(key) % 16384` → slot → node
- Client sabe qual node tem qual range de slots (gossip protocol)
- Se client manda request pro node errado, recebe **MOVED redirect**
- **Hot keys:** uma key muito acessada sobrecarrega 1 node
  - Soluções: (1) read replicas, (2) key splitting, (3) local in-memory cache

### Números
| Métrica | Valor |
|---------|-------|
| Throughput | ~100K-300K ops/sec (single node) |
| Latência | <1ms, tipicamente ~100-200 μs |
| Memória | Datasets devem caber na RAM. 1M keys × 1KB = ~1GB |

**Quando usar:** cache, counters, rate limits, sessões, leaderboards, distributed locks
**Quando NÃO usar:** durabilidade garantida, joins, datasets > RAM, analytics
**Pitch:** *"I'd use Redis as a caching layer for sub-ms reads, with TTL and LRU eviction"*

---

## PostgreSQL

**O que é:** banco de dados relacional, ACID, open-source. **Source of truth.**

**Quando usar em entrevista:**
- Dados estruturados com relacionamentos e constraints
- Precisa de UNIQUE, FK, CHECK constraints
- Transactions ACID

### Escalabilidade
| Nível | Técnica | Detalhe |
|-------|---------|---------|
| 1 | Vertical | Mais CPU/RAM |
| 2 | **Read replicas** | Replicação assíncrona. Delay ~ms. Trade-off: eventual consistency |
| 3 | Connection pooling | PgBouncer. Evita exaurir conexões |
| 4 | Partitioning | Dividir tabela por range (date) ou hash (user_id) |
| 5 | **Sharding** | Último recurso. SÓ quando single primary não aguenta (>10K writes/sec) |

### Índices
| Tipo | Uso |
|------|-----|
| B-tree (default) | Range queries, equality. O(log N) |
| GIN | Full-text search, JSONB |
| GiST | Geospatial (PostGIS) |

### Números
| Métrica | Valor |
|---------|-------|
| Simple inserts | 5,000-10,000/sec (single primary) |
| Indexed reads | 10,000-50,000/sec |
| Complex joins | 100-1,000/sec |

> 💡 *"Postgres handles 5-10K inserts/sec easily on single primary. Sharding would be premature at this scale."* → mostra maturidade

---

# 2. Padrões de Design (Patterns)

## Scaling Reads ⭐ (novo)

**Problema:** sistema tem muitas leituras e o banco principal não aguenta.

### Progressão de soluções (do mais simples ao mais complexo)

**NÍVEL 1 — Otimizar dentro do DB**
- Adicionar índices (B-tree para queries frequentes)
- Denormalizar dados (evitar joins caros — copiar dados redundantes)
- Materializar views para queries complexas recorrentes
- Otimizar queries (`EXPLAIN ANALYZE` para encontrar bottlenecks)

**NÍVEL 2 — Escalar horizontalmente o DB**
- **Read replicas:** replicação assíncrona do primary. App lê das replicas.
  - Mecanicamente: primary escreve WAL (Write-Ahead Log) → replica aplica WAL.
  - Trade-off: replica delay (ms-sec). Leitura pode retornar dado stale.
  - Quando ok: feeds, reviews, perfis. Quando NÃO ok: saldo bancário.
- Sharding por read pattern: dividir dados por tenant/região se queries são isoladas

**NÍVEL 3 — Cache externo**
- Redis/Memcached entre app e DB:
  `App → Redis (hit?) → se sim, retorna. Se não → Postgres → salva no Redis → retorna`

| Strategy | Como funciona | Trade-off |
|----------|---------------|-----------|
| **Cache-Aside (Lazy)** | App controla. Se miss, lê DB e popula cache | Simples, mas cold start lento |
| **Write-Through** | Toda write vai pro cache E pro DB | Cache sempre fresh, mas write mais lento |
| **Write-Behind** | Write vai pro cache, cache escreve no DB async | Rápido, mas pode perder dados |

- **CDN** para conteúdo estático (imagens, CSS, JS)
- **Cache stampede:** quando TTL expira e TODAS requests batem no DB
  - Soluções: (1) distributed lock, (2) probabilistic early expiration, (3) stale-while-revalidate

> 💡 *"Before adding infrastructure complexity, I'd first optimize the query and add proper indexes. If that's not enough for our QPS, I'd add read replicas."*

---

## Scaling Writes ⭐ (novo)

**Problema:** muitas escritas e o banco primary não aguenta.

**NÍVEL 1 — Otimizar o DB**
- Escolher o DB certo (SQL vs NoSQL). DynamoDB/Cassandra escalam writes melhor.
- Batch writes (1000 rows de uma vez vs 1000 inserts individuais)
- Desabilitar indexes desnecessários (cada index = overhead no write)

**NÍVEL 2 — Sharding/Partitioning**
- Dividir dados entre múltiplos DB nodes por partition key
- Partition key ideal: distribuição uniforme, queries não precisam cross-shard
- Ex: shard by user_id (bom), shard by country (ruim se 1 país tem 80% dos dados)
- **Hot key problem:** mesmo com sharding, 1 key recebe todas as writes
  - Solução: **key splitting** (`counter:123` → `counter:123:shard1..shardN`, soma ao ler)

**NÍVEL 3 — Write queue/buffer**
- Fila (Kafka/SQS) na frente do DB
- App escreve na fila (rápido) → worker consome e escreve no DB (throttled)
- Absorve picos. Trade-off: latência extra, eventual consistency.

**NÍVEL 4 — Hierarchical aggregation**
- Para contadores de alta escala: agregar em camadas
- Ex: 1000 servers contam localmente → a cada 1 sec enviam subtotais → aggregator soma
- Usado pelo YouTube para view counts

**RESHARDING** (pergunta clássica):
- **Consistent hashing:** minimiza redistribuição ao adicionar nodes
- Precisa de migration strategy (dual-write → switch → cleanup)

---

## Real-Time Updates ⭐ (novo)

**Problema:** como o servidor envia dados para o client em tempo real?

### Arquitetura "Two-Hop"
- **Hop 1:** Source → Server (como o server fica sabendo que algo mudou?)
- **Hop 2:** Server → Client (como o client recebe a atualização?)

### Hop 2 — Server → Client (5 opções)

| Protocolo | Como funciona | Pros | Contras | Usar para |
|-----------|---------------|------|---------|-----------|
| **Simple Polling** | Client faz GET a cada X sec | Simples, stateless | Desperdiça requests, alta latência | Dashboards, job status |
| **Long Polling** | Server segura conexão até ter dados | Menor latência | Conexões abertas, reconnect após cada resposta | Chat básico, notificações |
| **SSE** | Conexão HTTP unidirecional (server→client) | Simples, reconexão auto | Unidirecional, ~6 conexões/domínio | Feeds real-time, stock prices |
| **WebSocket** ⭐ | Conexão bidirecional persistente | Full-duplex, baixa latência | Stateful, sticky sessions | Chat, location, collaborative editing |
| **WebRTC** | Peer-to-peer direto | Menor latência possível | Complexo, NAT traversal | Video calls, screen sharing |

### WebSocket — como funciona mecanicamente
```
1. Client faz HTTP request com header "Upgrade: websocket"
2. Server aceita → conexão "upgrada" para WebSocket
3. Agora ambos podem enviar dados a qualquer momento (full-duplex)
4. Conexão fica aberta até client ou server fechar
```
> ⚠️ Scaling WebSocket: precisa de sticky sessions ou connection registry. Load balancer precisa suportar WS (ALB sim, CLB não).

### Hop 1 — Source → Server
1. **Polling do DB:** server faz query a cada X sec. Simples mas desperdiça resources.
2. **CDC (Change Data Capture):** DB envia stream de mudanças. Ex: Postgres WAL → Debezium → Kafka
3. **Pub/Sub:** Redis Pub/Sub ou Kafka. Serviço publica, server subscrito recebe.
4. **Consistent Hashing:** rotear updates para o server que mantém a conexão WS do client.

### Fan-Out Problem (muito importante para entrevistas)

Quando 1 evento precisa ser enviado para MUITOS clients/users.
Ex: celebridade posta foto → 10M followers precisam ver no feed.
Ex DoorDash: review popular recebe 10K upvotes → precisa atualizar ranking.

#### Fan-out on WRITE (push model)

**Como funciona mecanicamente:**
```
User A posta review → sistema escreve na "inbox" de CADA follower

1. User A publica review
2. Sistema busca todos os followers de User A: [User B, User C, ..., User Z]
3. Para CADA follower:
   INSERT INTO feed (user_id, review_id, created_at) VALUES (B, 123, now());
   INSERT INTO feed (user_id, review_id, created_at) VALUES (C, 123, now());
   ... (repete para cada follower)
4. Quando User B abre o feed: SELECT * FROM feed WHERE user_id = B ORDER BY created_at
   → Rápido! Já está tudo pré-computado.
```

**Números:**
- User com 500 followers → 1 post = 500 writes. Ok.
- Celebridade com 10M followers → 1 post = **10M writes**. Demora minutos!

| Pros | Contras |
|------|---------|
| Leitura muito rápida (O(1) por user) | Write amplification massiva |
| Feed sempre pronto quando user abre | Celebridades = bottleneck |
| Simples de implementar a leitura | Storage alto (N cópias do mesmo dado) |

**Quando usar:** users com poucos followers (<10K), sistemas onde leitura rápida é crítica

#### Fan-out on READ (pull model)

**Como funciona mecanicamente:**
```
User A posta review → sistema escreve APENAS no perfil de User A

1. User A publica review
2. INSERT INTO reviews (user_id, content) VALUES (A, '...');
   → 1 write apenas. Rápido.
3. Quando User B abre o feed:
   a. Buscar quem User B segue: SELECT following FROM follows WHERE user_id = B
      → Retorna [User A, User C, User D, ...]
   b. Para CADA seguido, buscar posts recentes:
      SELECT * FROM reviews WHERE user_id IN (A, C, D, ...) ORDER BY created_at LIMIT 50
   c. Mergear e ordenar todos os resultados
   d. Retornar para User B
```

**Números:**
- User segue 200 pessoas → abrir feed = 200 queries (ou 1 query com IN clause grande)
- Se cada query demora 5ms → 200 × 5ms = **1 segundo** para carregar feed. Lento!

| Pros | Contras |
|------|---------|
| Write rápido (1 write apenas) | Leitura lenta (merge de N fontes) |
| Sem write amplification | Latência alta ao abrir feed |
| Storage eficiente | Mais complexo no read path |

**Quando usar:** celebridades, users com muitos followers, sistemas write-heavy

#### HYBRID (o que Twitter/Instagram/DoorDash fazem) ⭐

**Como funciona mecanicamente:**
```
Classificar users em 2 categorias:
- Users normais (< 10K followers) → fan-out on WRITE
- Celebridades (> 10K followers) → fan-out on READ

Quando User B abre o feed:
1. Ler inbox pré-computada (posts de users normais que B segue)
   → Rápido, já estava pronto
2. Buscar posts recentes das celebridades que B segue
   → Poucos (B segue talvez 5-10 celebridades)
3. Mergear os dois resultados e ordenar por timestamp
4. Retornar feed completo
```

**Por que funciona:**
- 99% dos users são normais → fan-out on write funciona bem
- 1% são celebridades → fan-out on read para poucos users é rápido
- O merge final é barato (inbox + poucos pulls)

| Pros | Contras |
|------|---------|
| Balanceia write e read | Mais complexo de implementar |
| Resolve o problema da celebridade | Precisa classificar users (threshold) |
| Escalável para bilhões de users | Duas code paths diferentes |

#### Exemplo aplicado: DoorDash Food Reviews

No Food Reviews, o fan-out aparece quando:
- Um review popular precisa aparecer no **top reviews** de um produto
- Muitos users abrem a mesma página de produto ao mesmo tempo

**Solução no nosso design:**
- Não é fan-out clássico (não temos followers), mas o princípio é similar
- **Redis Sorted Set** funciona como fan-out on write para o ranking:
  ```
  Cada upvote → ZADD product:42:reviews {new_score} "review:123"
  Quando user abre produto → ZREVRANGE product:42:reviews 0 9 (top 10)
  ```
- O ranking está **sempre pré-computado** no Redis (push model)
- A leitura é O(log N) — sub-millisecond
- Isso é efetivamente **fan-out on write** para o ranking

---

## Multi-Step Process

**O que é:** processos com múltiplas etapas que não podem falhar no meio.
**Exemplo:** `order created → payment → picking → confirmation → delivery`

### 3 abordagens
1. **Servidor único:** chamadas encadeadas em memória. Simples, mas se cair perde estado.
2. **Event Sourcing:** cada serviço publica e consome eventos com contratos versionados.
3. **Durable Workflows (Temporal/Cadence):** funções determinísticas com estado em banco temporal. Se cair, reinicia de onde parou.

> ⚠️ **COMPENSATING TRANSACTIONS** — quando um step falha, os steps anteriores precisam de rollback (ex: estornar pagamento se picking falhou)

**Bom para:** sistemas financeiros, processos com etapas manuais
**Não é bom para:** processamento async simples, alta carga de leitura

---

## Contention

**O que é:** múltiplos processos competindo pelo mesmo recurso.
**Exemplos:** tickets de show, transferências bancárias, leilões.

**Pergunta-chave: o dado cabe em um único banco de dados?**

### SE SIM (single database)

#### 1. Pessimistic Locking (SELECT FOR UPDATE)

**Como funciona mecanicamente:**
```sql
BEGIN;
SELECT * FROM tickets WHERE id = 1 FOR UPDATE;
-- Neste momento, a linha id=1 está LOCKADA.
-- Nenhuma outra transação consegue ler com FOR UPDATE ou modificar esta linha.
UPDATE tickets SET status = 'sold', buyer_id = 123 WHERE id = 1;
COMMIT;  -- Lock é liberado
```
Se outra transação tentar `SELECT FOR UPDATE` na mesma linha, ela **ESPERA** (bloqueada) até o COMMIT da primeira.

**Trade-off:** seguro, mas pode causar deadlocks e reduz throughput.
**Usar quando:** conflitos são FREQUENTES, dados são CRÍTICOS (dinheiro, tickets)

#### 2. Optimistic Concurrency Control (OCC)

**Como funciona mecanicamente:**
```sql
-- Lê o dado com a versão atual
SELECT *, version FROM tickets WHERE id = 1;  -- version = 5
-- Processa no application level
-- Tenta atualizar, mas SÓ SE a versão não mudou
UPDATE tickets SET status='sold', buyer_id=123, version=6
  WHERE id=1 AND version=5;
-- Se 0 rows affected → alguém mudou antes. Retry!
-- Se 1 row affected → sucesso.
```

**Trade-off:** melhor throughput, mas retries frequentes se alta contenção.
**Usar quando:** conflitos são RAROS (editar perfil, atualizar preferências)

### SE NÃO (distributed/multi-database)

#### 1. Saga Pattern ⭐ (MUITO IMPORTANTE para sistemas de pagamento)

**O que é:** sequência de transações locais independentes. Cada step é um COMMIT completo no seu próprio banco. Se um step falha, executa **COMPENSATING TRANSACTIONS** nos steps anteriores (rollback lógico).

**Diferença chave vs transação normal:**
```
Transação ACID: BEGIN → op1 → op2 → op3 → COMMIT (tudo ou nada, 1 banco)
Saga:           op1 COMMIT → op2 COMMIT → op3 COMMIT (cada um independente, N bancos)
                Se op3 falha: compensate op2 → compensate op1
```

##### Exemplo mecânico — Sistema de Pagamento (DoorDash payout)

**Contexto:** reviewer atingiu threshold de upvotes, precisa receber pagamento.
**Serviços:** EarningsService (DB1), WalletService (DB2), PaymentGateway (externo)

**FLUXO FELIZ (tudo dá certo):**

**Step 1: EarningsService**
```sql
INSERT INTO payouts (review_id, user_id, amount, status)
  VALUES (123, 456, 50.00, 'pending');
COMMIT;  -- transação local completa
-- → Publica evento: "payout_initiated"
```

**Step 2: WalletService** (ouve "payout_initiated")
```sql
UPDATE wallets SET balance = balance + 50.00 WHERE user_id = 456;
INSERT INTO wallet_transactions (user_id, amount, type, payout_id)
  VALUES (456, 50.00, 'credit', 123);
COMMIT;  -- transação local completa
-- → Publica evento: "wallet_credited"
```

**Step 3: PaymentGateway** (ouve "wallet_credited")
```
POST /transfers { amount: 5000, destination: user_stripe_id }
Se sucesso → publica "payment_completed"
```

**Step 4: EarningsService** (ouve "payment_completed")
```sql
UPDATE payouts SET status = 'completed' WHERE id = 123;
COMMIT;
-- → Fim do saga. Tudo deu certo.
```

**FLUXO COM FALHA (Step 3 falha — Stripe retorna erro):**
- Step 1: ✅ payout criado (status='pending')
- Step 2: ✅ wallet creditado (+50.00)
- Step 3: ❌ Stripe falhou!

**COMPENSATIONS (rollback lógico, na ordem INVERSA):**

Compensate Step 2 — WalletService:
```sql
UPDATE wallets SET balance = balance - 50.00 WHERE user_id = 456;
INSERT INTO wallet_transactions (user_id, amount, type, payout_id)
  VALUES (456, -50.00, 'debit_reversal', 123);
COMMIT;
```

Compensate Step 1 — EarningsService:
```sql
UPDATE payouts SET status = 'failed', failure_reason = 'payment_declined'
  WHERE id = 123;
COMMIT;
```

> ⚠️ **IMPORTANTE:** compensations NÃO são DELETE. São novas transações que REVERTEM o efeito lógico. Mantém audit trail completo.

##### 2 modos de coordenação

| Modo | Como funciona | Pros | Contras | Quando usar |
|------|---------------|------|---------|-------------|
| **Choreography** | Cada serviço ouve eventos e decide sozinho | Desacoplado, sem SPOF | Difícil debugar, sem visão global | Sagas simples (2-3 steps) |
| **Orchestration** ⭐ | Orchestrator central coordena os steps | Explícito, fácil debugar/monitorar | SPOF (mitigar com HA) | Sagas complexas, **PAGAMENTOS** |

**Orchestration — pseudocódigo:**
```python
def execute_payout(data):
    result1 = earnings_service.create_payout(data)
    if result1.success:
        result2 = wallet_service.credit(data)
        if result2.success:
            result3 = payment_gateway.transfer(data)
            if result3.failure:
                wallet_service.compensate_credit(data)    # rollback step 2
                earnings_service.mark_failed(data)         # rollback step 1
```

##### Idempotência é OBRIGATÓRIA

Cada step pode ser executado mais de 1 vez (retry após falha). Sem idempotência → **pagamento duplicado**.

**Como garantir:**
- Idempotency key: `(payout_id, step_name)` como UNIQUE no banco
- Antes de executar: `SELECT WHERE idempotency_key = X`
  - Se existe → já executou, retorna resultado anterior
  - Se não existe → executa e salva resultado

##### Retry Strategy
- **Exponential backoff:** 1s → 2s → 4s → 8s → ...
- **Max retries:** 3-5 tentativas
- **Após max retries:** manda para **DLQ** (Dead Letter Queue) para análise manual
- Para pagamentos: **SEMPRE ter DLQ**. Dinheiro não pode se perder silenciosamente.

##### Garantias do Saga
- **Eventual consistency:** entre steps, sistema está em estado intermediário
- **Atomicidade "lógica":** ou tudo completa ou tudo é compensado
- **NÃO tem isolamento:** outros processos podem ver estado intermediário (ok para pagamentos — status='pending' é visível)

##### Reconciliação ⭐ (a rede de segurança final)

Mesmo com saga + idempotência + DLQ, coisas podem dar errado:
- Compensation falhou silenciosamente
- Rede caiu entre step 2 e step 3, evento perdido
- Bug no código, saldo inconsistente
- Payment gateway cobrou mas não retornou resposta (timeout)

**O que é:** processo batch que COMPARA estados entre sistemas e encontra inconsistências.

**Como funciona mecanicamente:**

**Reconciliation Job** (roda a cada X horas, tipicamente 1x/dia):

**1. EXTRAIR:** puxa registros de cada sistema
```sql
-- Do EarningsService:
SELECT * FROM payouts WHERE date = today;
-- Do WalletService:
SELECT * FROM wallet_transactions WHERE date = today;
-- Do PaymentGateway:
GET /transfers?created[gte]=today
```

**2. COMPARAR** (join lógico por payout_id):

| earnings_status | wallet_status | gateway_status | Problema? |
|----------------|---------------|----------------|-----------|
| completed | credited | transferred | ✅ OK |
| completed | credited | NOT FOUND | ❌ Pagamento perdido |
| pending | credited | transferred | ❌ Status desatualizado |
| failed | credited | NOT FOUND | ❌ Wallet não compensou |
| completed | NOT FOUND | transferred | ❌ Wallet perdeu credit |

**3. GERAR** relatório de discrepâncias:
- **Automático:** corrigir casos simples (atualizar status)
- **Manual:** alertar equipe para casos complexos
- **Métricas:** % de inconsistências (target: <0.01%)

**4. CORRIGIR:**
- **Auto-fix:** gateway confirma mas status='pending' → `UPDATE payouts SET status='completed'`
- **Manual-fix:** wallet creditou mas gateway não transferiu → equipe decide
- **DLQ replay:** reprocessar eventos que falharam

##### Tipos de reconciliação

| Tipo | O que compara | Frequência |
|------|---------------|------------|
| **Internal** | Seus serviços entre si (EarningsDB vs WalletDB) | A cada hora |
| **External** | Seu sistema vs terceiro (WalletDB vs Stripe) | Diário (T+1) |
| **Ledger-based** | Double-entry: debit + credit devem somar zero | Contínuo |

> 💡 **Ledger-based:** cada transação tem DEBIT e CREDIT que somam zero.
> Ex: payout $50 → debit empresa + credit reviewer = $0. Se soma ≠ 0 → inconsistência.
> Usado por: Stripe, Wise, Nubank, qualquer fintech séria.

**Pitch reconciliação:** *"I'd add a reconciliation job as the final safety net. It runs daily, compares our internal records with the payment gateway, and flags any mismatches."*

**Pitch saga completo:** *"For the payout flow, I'd use an orchestrated saga. Each step is a committed transaction with a compensating action. If the payment gateway fails, we reverse the wallet credit and mark the payout as failed. Idempotency keys prevent duplicate payments. And as a final safety net, a daily reconciliation job catches any edge cases."*

**Camada completa de defesa:**
1. **Saga** — happy path + compensations
2. **Idempotência** — previne duplicatas
3. **DLQ** — captura falhas após retries
4. **Reconciliação** — rede de segurança final

---

#### 2. Two-Phase Commit (2PC)

**Como funciona mecanicamente:**
```
COORDINATOR envia para todos os PARTICIPANTS:

Phase 1 (PREPARE):
  Coordinator: "Preparem a transação"
  Participant A: executa localmente, NÃO commita, responde "READY"
  Participant B: executa localmente, NÃO commita, responde "READY"

Phase 2 (COMMIT):
  Se todos READY → Coordinator: "COMMIT todos"
  Se algum ABORT → Coordinator: "ROLLBACK todos"
```

> ⚠️ **PROBLEMA FATAL:** se coordinator cair entre phase 1 e 2, todos os participants ficam com transações ABERTAS. Deadlock distribuído. **NÃO usar em microservices.**

**Pitch:** *"For distributed transactions, I'd use Saga over 2PC — it's non-blocking, more resilient, and scales better for microservices"*

---

## Outbox Pattern ⭐ (aprendi no mock — fixando)

**O que é:** garantir que evento SEMPRE é publicado após write no banco.

**Problema:** write no Postgres + publish no Kafka = 2 operações em sistemas diferentes. Se publish falha, evento se perdeu.

### Como funciona mecanicamente

**1. Na MESMA transação:**
```sql
BEGIN;
  INSERT INTO reviews (id, user_id, rating, comment) VALUES (...);
  INSERT INTO outbox (id, event_type, payload, created_at, published)
    VALUES (uuid, 'review_created', '{"review_id":...}', now(), false);
COMMIT;
-- → Transação ACID garante: ambos escritos ou nenhum.
```

**2. Outbox Poller** (processo separado, roda a cada 100-500ms):
```sql
SELECT * FROM outbox WHERE published = false ORDER BY created_at LIMIT 100;
-- Para cada evento: publica no Kafka
-- Se ok: UPDATE outbox SET published = true WHERE id = X;
-- Se falha: tenta no próximo ciclo
```

**3. Alternativa ao poller:** CDC (Change Data Capture)
`Postgres WAL → Debezium → Kafka` (automaticamente, sem polling)
Mais elegante, menor latência, mas mais infra.

**Trade-off:** eventual consistency (delay ms/sec), mas **NUNCA perde evento**.
**Pitch:** *"I'd use the outbox pattern — write the record and the event in the same transaction, then a poller publishes to Kafka. Guaranteed delivery."*

---

## Async After 200 ⭐ (aprendi no mock — fixando)

**O que é:** retornar 200 IMEDIATAMENTE após source of truth write. Resto é async.

### Como funciona mecanicamente

**ANTES (3 sync operations — ERRADO):**
```
Request → [write Postgres] → [INCR Redis] → [publish Queue] → Response 200
Latência: 5ms + 0.5ms + 2ms = 7.5ms
Se Redis lento (50ms): usuário espera 55.5ms
Se Queue down: request FALHA
```

**DEPOIS (1 sync + rest async — CORRETO):**
```
Request → [write Postgres + write outbox] → Response 200
                                             ↓ (async)
                                       [poller → publish Queue]
                                       [worker → INCR Redis]
Latência para user: 5ms (só Postgres)
```

**Por que funciona:**
- Postgres é source of truth. Se está lá, o dado existe.
- Redis é CACHE — pode ser recalculado
- Queue é async por natureza

> 💡 **Regra:** *"Write to source of truth, return 200, do everything else async"*

---

## Token Bucket — Rate Limiting Algorithm

**O que é:** algoritmo de rate limiting que permite bursts controlados.

### Como funciona mecanicamente — passo a passo

**Configuração:** `capacity=100, refill_rate=10/min`

**Estado armazenado (por user, no Redis):**
```
Key: rate_limit:{user_id}
Value: { tokens: 100, last_refill: 1740000000 }
```

**Quando chega um request:**
1. Ler estado atual: `tokens=85, last_refill=1740000060`
2. Calcular tokens acumulados desde last_refill:
   ```
   elapsed = now - last_refill = 30 seconds
   new_tokens = elapsed × (refill_rate / 60) = 30 × (10/60) = 5 tokens
   ```
3. Atualizar: `min(tokens + new_tokens, capacity) = min(85+5, 100) = 90`
4. Tem token?
   - **SIM** (90 > 0): `tokens = 90 - 1 = 89`. Permitir. Atualizar Redis.
   - **NÃO** (0): Rejeitar com `429 Too Many Requests`.
5. Salvar: `{ tokens: 89, last_refill: now }`

> ⭐ **O REFILL NÃO É UM PROCESSO SEPARADO** — é calculado em tempo de execução!
> Cada request calcula quantos tokens acumularam desde a última vez.
> Isso é chamado de **"lazy refill"** — nenhum background job necessário.

### Implementação atômica com Redis (Lua script)
```lua
local key = KEYS[1]
local capacity = tonumber(ARGV[1])       -- 100
local refill_rate = tonumber(ARGV[2])    -- 10 per minute
local now = tonumber(ARGV[3])
local tokens = redis.call('HGET', key, 'tokens') or capacity
local last = redis.call('HGET', key, 'last_refill') or now
local elapsed = now - last
tokens = math.min(tokens + elapsed * refill_rate / 60, capacity)
if tokens >= 1 then
  tokens = tokens - 1
  redis.call('HSET', key, 'tokens', tokens, 'last_refill', now)
  return 1  -- allowed
else
  return 0  -- rejected
end
```

### Por que é melhor que Fixed/Sliding Window
- **Fixed Window:** user faz 99 req no segundo 59 + 100 no segundo 61 = 199 em 2 seg. Boundary burst!
- **Token Bucket:** capacity é o MÁXIMO de burst. Depois, limitado pela refill rate.
- Permite **bursts controlados**: user idle por 10 min acumula tokens
- Configs diferentes por endpoint: `/api/search` (100/min), `/api/payment` (10/min)

---

## CAP Theorem

Em sistema distribuído, escolha 2 de 3:
- **C**onsistency: todos os nós veem o mesmo dado
- **A**vailability: toda request recebe resposta
- **P**artition tolerance: funciona com falha de rede

Partições SEMPRE podem acontecer → escolha real é **CP vs AP**:

| Escolha | Comportamento | Exemplo |
|---------|---------------|---------|
| **CP** | Pode ficar indisponível durante partição | Pagamentos, saldo, inventory |
| **AP** | Responde mas dado pode estar stale | Reviews, feeds, likes, cache |

> 💡 *"For reviews, AP — eventual consistency is fine. For payouts, CP — consistency is critical to avoid duplicate payments"*

---

# 3. Problemas de System Design Praticados

## Rate Limiter
- **Onde vive:** API Gateway (borda). NÃO dentro de cada serviço.
- **Algoritmos:** Fixed Window, Sliding Window Log/Counter, Token Bucket
- **Storage:** Redis (sub-ms, atômico, distribuído)
- **Fail mode:** fail-open (permite tudo) vs fail-closed (bloqueia tudo)
- **Trade-off:** Availability > Consistency

## Uber / Ride Matching
- **Fluxo:** Rider → Fare Service → Matching Service → Driver notification
- **Entidades:** rider, driver, trip, fare, location
- **Gaps que preciso fixar:**
  - Geospatial: Geohash/QuadTree/S2 Cells
  - Real-time: WebSocket para location streaming
  - ETA: graph algorithms + trânsito
  - Surge pricing: demand/supply ratio

## Food Reviews + Payouts (mock 24/fev — Borderline Hire)
- **Fortes:** entities, APIs, Redis INCR, queue separation, DLQ, idempotency
- **Gaps:** (1) napkin math, (2) async critical path, (3) wrap-up trade-offs
- **Wrap-up modelo (MEMORIZAR):**
  *"The key trade-off is eventual consistency on vote counts — users might see slightly stale counts, but we get sub-100ms response times. For payouts, strong consistency with unique constraint prevents duplicates, accepting higher latency. With more time: notification service, fraud detection."*

## Job Scheduler
- **Entidades:** task, job, execution, schedule, user
- **Componentes:** JobService → SchedulerService → Queue → WorkerService
- **Scaling:** partitioned scheduling `hash(job_id) % N`, auto-scale workers, DLQ

---

# 4. Napkin Math — Referência Rápida

### Latências
| Operação | Latência |
|----------|----------|
| L1 cache | 0.5 ns |
| RAM | 100 ns |
| SSD read | 150 μs |
| Network round trip (datacenter) | 500 μs |
| Redis | <1 ms |
| Postgres simple | 1-5 ms |
| Postgres complex | 10-100 ms |

### Throughput (single node)
| Sistema | Throughput |
|---------|-----------|
| Redis | 100K-300K ops/sec |
| Postgres inserts | 5,000-10,000/sec |
| Postgres indexed reads | 10,000-50,000/sec |
| Kafka | 1M+ msgs/sec (cluster) |

### Storage
| Escala | Tamanho |
|--------|---------|
| 1M rows × 1KB | 1 GB |
| 1B rows × 1KB | 1 TB |

### QPS Calculation
```
DAU / 86,400 = average QPS
Peak = 3-5x average
Ex: 30M orders/day = ~350 QPS avg, ~1,750 peak
```

---

# 5. Framework SD (usar em TODA entrevista)

| Fase | Tempo | O que fazer |
|------|-------|-------------|
| 1. Requirements | 5 min | Functional + Non-functional. **PERGUNTAR ESCALA!** |
| 2. Core Entities | 3 min | Entidades + relacionamentos |
| 3. API Design | 5 min | Endpoints principais (REST) |
| 4. High-Level | 5 min | Diagrama com componentes |
| 5. Deep Dive | 25 min | 2-3 componentes. **AQUI mostra senioridade.** |
| 6. Scaling | 10 min | Bottlenecks + números + trade-offs |
| 7. Wrap-up | 5 min | Resumir decisões + o que faria com mais tempo |

### Regras
- ✅ SEMPRE perguntar números (QPS, users, storage)
- ✅ SEMPRE napkin math ANTES de propor scaling
- ✅ SEMPRE articular trade-offs: *"We chose X over Y because Z, accepting W"*
- ✅ SEMPRE estruturar: *"There are N things: first... second... third..."*
- ✅ Source of truth write → return 200 → rest is async
- ❌ Não propor sharding se single node aguenta os números

---

# 6. Decision Cards

| Tool/Pattern | Quando usar | Quando NÃO usar |
|--------------|-------------|-----------------|
| **Redis** | Cache, counters, rate limit, locks | Durabilidade, joins, >RAM |
| **Kafka** | Event streaming, desacoplamento | Req-response, baixo volume |
| **PostgreSQL** | Source of truth, ACID, relationships | >10K writes/sec, no relations |
| **Outbox** | Write + event na mesma transação | Quando eventual consist. ≠ ok |
| **Async after 200** | Side effects não essenciais | User PRECISA do resultado |
| **Saga** | Transações distribuídas | Tudo cabe em 1 banco |
| **2PC** | Quase nunca em microservices | Sempre que puder usar Saga |
| **Pessimistic Lock** | Conflitos frequentes | Baixa contenção |
| **OCC** | Conflitos raros | Alta contenção |
| **Token Bucket** | Rate limit com bursts | Fixed window basta |
| **Sorted Set** | Leaderboards, top-N | Dados com joins |
| **DLQ** | Pagamentos, processos críticos | Eventos descartáveis |
| **WebSocket** | Real-time bidirecional | Unidirecional (usar SSE) |
| **SSE** | Real-time server→client only | Client precisa enviar dados |
| **Read Replicas** | Read-heavy, tolera stale | Precisa strong consistency |
| **Cache-Aside** | Read-heavy, miss tolerável | Write-heavy |
| **Fan-out on Write** | Poucos followers | Celebridades (write amplif.) |
| **Fan-out on Read** | Celebridades | Users normais (leitura lenta) |
| **Reconciliação** | Pagamentos, dados financeiros | Inconsistência é aceitável |
 1. The live donation counter

  You're using INCR after Stripe success. But the requirement was near real-time counter visible to all users on
  the page. How do millions of users SEE the counter update? They're all on the donations page — do they poll?
  WebSocket? SSE? Which one and why?

R: isso nao estava no requerimentos, mas se voce esta falando para fazermos agora, podemos ter duas abordagens:
1 - manter a agregacao por charity, e ter um worker separado que agrega a cada X segundos todos os valores totais da caridade e manda para o front end via sse
2 - quando o transaction worker incrementa o valor da charity, tambem podemos ter uma outra chave(campaign_id) que incrementamos o valor total

  2. Step 2 — you said atomic transaction with INSERT donation + INSERT transaction

  Why are you creating the transaction record BEFORE calling Stripe? The transaction should be created by the
  worker AFTER it picks up the job. Otherwise if the worker never picks it up, you have an orphaned transaction
  record in INITIATED state forever. What's your reasoning?

R estamos criando uma transacao para manter todo o historico, pois caso ocorra uma falha com o stripe, eu posso marcar que aquela transacao
nao foi efetuada e colocar ela na fila de DQL para fazer a reconsiliacao depois, isso serve tambem para termos toda a auditoria das doacoes em caso de governanca interna
E se o worker nao pegou, quer dizer que eu tive uma falha antes de enviar para o stripe, e por isso eu posso reprocessar a transacao

3 Campaign ends in 24-48 hours
  What happens to in-flight donations when the campaign closes? User clicks donate at hour 47:59, payment
  processes at hour 48:01. Is it accepted or rejected? How do you handle this edge case?

Bom ponto, realmente nao coloque isso. E talvez a melhor abordagem para isso é colocar uma chave no redis com um TTL
de 48. Todas as requisicoes que entram na aplicacao passam por essa chave, e se ela for valida, a requisicao segue,
se ela ja foi expirada, a requisicao retorna uma mensagem dizendo que a campanha acabou. Assim a gente protege a aplicacao de
receber requisicoes e ter que validar essa regra toda vez

Now, scaling question. It's hour 1 of the campaign. A celebrity tweets "Donate on DoorDash!" and
  your traffic spikes 50x — from 8 QPS to 400 QPS in minutes. Millions hitting the page.

Following the data flow:
Redis to check campaign data can handle with 400qps
Load balancer will route the requests to DonationService that is deployad in AKS pods and can slace based on requests/cpu/memory
Postgres write: can handle with 5-10k writes per seconds, so this is ok also
Postgres read: can handle with 50-100k reads per seconds, but will be important to create a index in some specific tables like charity and donations. I dont think its necesasry to create read replicas
One thing that we can scale its the TransactionWorker to suport 50x more transactions, so we can also scale horizontaly
And finally for redis just in case we can have a HA, but redis will be also fine because will suport 100-300k ops sec

functional req
customer should be able to see where the drivers is in real time on map
driver should be able to send location informations to the user

nonfunctional req
availability > consistent its ok to lose one lat long from the driver and have eventual consistency
driver should send the locations every 2-3 seconds with low latency
customer should see the locations with low latency

numbers

10m / 10000k = 100QPS
30m active order * 60 = 1800sec
100 * 1800 = 18000 sessions
write qps = 18000 * 0.5 = 90000
peak = 90000 * 3 = 270000

with this numbers i can see that relational database will not handle with that
we need a stream(kafka, etc)
we need  in memory database due latency reqs
we need sharding
we need a real time update for the customers(websocket or sse)

core entities
order = id, amount, customer_id...
customer = id, name, document, phone..
driver = id, name, document, phone..
location event = id, lat, long, order_id, customer_id, driver_id...

apis
post -> /drivers/location
requests = {
  driver_id = xx,
  order_id = xx,
  lat = xx,
  long = xx,
  timestamp = xx
}

response = {
  "ok"
}

get -> /order/:orderId
response = {
  order_id = xx,
  status = xx,
  driver_id = xx,
}

get -> /order/:orderId/location
response = {
  lat = xx,
  long = xx,
  driver_id = xx,
}

wss:/order/:orderId/location/realtime
response = {
  lat = xx,
  long = xx,
  driver_id = xx,
}


hdl
Componentes
🔹 Edge Layer

Load Balancer

API Gateway

🔹 Application Layer

Location API

Order API

WebSocket Realtime Gateway

Location Processor

🔹 Data & Messaging

Kafka (driver-location topic)

Redis (latest driver state)

PostgreSQL (orders, drivers, customers)

2️⃣ Arquitetura Geral
                        ┌────────────────────────┐
                        │      Driver App        │
                        └────────────┬───────────┘
                                     │
                                     ▼
                             ┌──────────────┐
                             │ LoadBalancer │
                             └──────────────┘
                                     │
                                     ▼
                             ┌──────────────┐
                             │ API Gateway  │
                             └──────────────┘
                                     │
                                     ▼
                             ┌──────────────┐
                             │ Location API │
                             └──────────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │ Kafka Topic          │
                          │ driver-location      │
                          │ (N partitions)       │
                          └──────────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                                 ▼
         ┌─────────────────────┐           ┌──────────────────────┐
         │ Location Processor  │           │ WebSocket Gateway    │
         └─────────────────────┘           └──────────────────────┘
                    │                                 │
                    ▼                                 ▼
             ┌──────────────┐                  ┌──────────────┐
             │   Redis      │                  │ Customer App │
             │ latest state │                  │  (WebSocket) │
             └──────────────┘                  └──────────────┘
3️⃣ Data Flow — Driver
Driver App
   ↓
Load Balancer
   ↓
API Gateway
   ↓
Location API
   ↓
Kafka (partition by driver_id)

4️⃣ Data Flow — Internal Processing
Kafka
   ↓
Location Processor
   ↓
Redis
(driver:{id}:location = latest lat/lng)

5️⃣ Data Flow — Customer (Initial Request)
Customer App
   ↓
Load Balancer
   ↓
API Gateway
   ↓
Order API
   ↓
PostgreSQL (get driver_id)
   ↓
Redis (get latest location)
   ↓
Return initial lat/lng

6️⃣ Data Flow — Customer (Realtime)
Customer App
   ↓
Load Balancer (WebSocket support)
   ↓
WebSocket Gateway
   ↓
(Register order_id → connection)

new location:
Kafka
   ↓
WebSocket Gateway (consumer group)
   ↓
Filter interested connections
   ↓
Push via WebSocket
   ↓. 
Customer App updates map

deep dives
how we can scale and availability the websockets?
we can have a loadbalancer with distributed connections to route the request to websockets
we can also have websockets deployed on kubernetes and have HPA

redis will support this massive writes every time for update the driver location?
we can go to a redis cluster strategy sharded


how redis will manage and ttl and read scale?
we can have a 30 sec ttl. if the driver dont send anything we remove the key and clean the memory
also with redis cluster we can have a read replicas to support shard by driver_id

how we will scale kafka? supposed we have more order in the future, just one topic will handle?
one topic will be ok. we need just to check the partition strategy, brokers e consumer groups
we can incrase the numer of partition to suport horizontal scalability or add more brokers
also if we have more than 1 location, we can create topics based on regions

1) 20M users, 5% DAU, each user sends 10 messages/day. Message = 500 bytes. Write QPS? Storage/month?           
messages day = 1m dau * 10 = 10m
write qps = 10m / 100k = 100
storage month = 10m * 5gb dia; ~150gbmes

2) 3M orders/day, each order triggers 2 Kafka events, each event = 1KB. Events/sec?
Storage/week?
3m * 2 = 6m events
6m / 100k = 60qps

3) 200K concurrent drivers, each sends GPS ping every 3 seconds. Pings/sec? Each ping = 100
bytes, bandwidth?

200k / 3 = 66pings/sec
66 * 100 = 6k/sec bandwidth

1 KB  ≈ 10³ bytes  (1.000)
1 MB  ≈ 10⁶ bytes
1 GB  ≈ 10⁹ bytes
1 TB  ≈ 10¹² bytes