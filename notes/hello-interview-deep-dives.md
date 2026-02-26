# Hello Interview - System Design Deep Dives (Reference)

Source: hellointerview.com | Extracted: 2026-02-25

---

## 1. SCALING READS

**Source:** https://www.hellointerview.com/learn/system-design/patterns/scaling-reads

### The Core Problem

Read traffic vastly exceeds write traffic. Instagram feed = 100+ queries per request, users post once/day. Twitter = thousands of reads per tweet. YouTube = billions of views vs millions of uploads. Read-to-write ratios: **10:1 baseline**, **100:1+ for content platforms**.

Physics constraint: DB performance hits hard limits -- CPU speed, memory capacity, disk I/O bandwidth. Code optimization cannot overcome hardware limits.

### Strategy 1: Optimize Within the Database

**Indexing**
- Creates lookup structures that eliminate full table scans
- Accelerates queries on frequently accessed columns
- Trade-off: increased storage, slower writes (index maintenance)

**Vertical Scaling (Hardware)**
- More CPU cores, RAM, faster SSDs
- Temporary relief; ceiling when dataset outgrows single machine

**Denormalization**
- Duplicate data across tables to eliminate expensive JOINs
- Reduces query complexity
- Trade-off: more storage, synchronization complexity (data can get out of sync)

### Strategy 2: Scale Database Horizontally

**Read Replicas**
- Primary DB handles writes; replica nodes serve read-only queries
- Replication is **asynchronous** -- replicas may serve stale data (replica lag)
- Application routes: reads -> replicas, writes -> primary
- Math: 1 primary + 3 replicas = **3x read capacity**
- Risk: consistency issues during rapid updates (user writes, then reads from stale replica)

**Database Sharding**
- Partition data across multiple DB instances (consistent hashing or range-based keys)
- Each shard handles a subset of data
- Enables "infinite" horizontal scaling
- Trade-off: cross-shard queries need aggregation layer; operational complexity increases significantly

### Strategy 3: External Caching Layers

**Application-Level Cache (Redis, Memcached)**
- Store hot data in memory between app and DB
- Mechanical flow: request -> check cache -> HIT: return cached data / MISS: query DB -> populate cache -> return
- Dramatically reduces DB load for frequently accessed data
- Challenge: **invalidation** -- stale data served until expiry or explicit deletion

**Cache Stampede / Thundering Herd**
- Problem: cache entry expires -> ALL concurrent requests miss cache -> ALL hit DB simultaneously
- Solutions:
  - **Distributed locking**: only first requester rebuilds; others wait
  - **Probabilistic early expiration**: recompute at ~80% of TTL; random jitter prevents simultaneous recompute
  - **Write-through cache**: update cache on every write (no expiry-based invalidation)

**Cache Invalidation Strategies**
- **TTL-based**: simple but introduces staleness window
- **Event-driven**: write operations publish cache-clear messages via pub/sub
- Trade-off: complex infrastructure vs. acceptable staleness window

**CDN / Edge Caching**
- Geographically distributed servers cache static/semi-static content near users
- Eliminates origin server round trips
- Latency: hundreds of ms -> tens of ms

### Key Numbers
- 10:1 minimum read-write ratio (baseline)
- 100:1+ for content platforms
- 100+ DB queries per single Instagram feed load
- Single tweet -> thousands of concurrent reads

### Interview Scenarios Using This Pattern
Ticketmaster, Bit.ly, Instagram, Facebook News Feed, YouTube Top K, Yelp, Distributed Cache, Rate Limiter, YouTube, Facebook Post Search, Local Delivery Service, News Aggregator, Metrics Monitoring

---

## 2. SCALING WRITES

**Source:** https://www.hellointerview.com/learn/system-design/patterns/scaling-writes

### The Core Problem

Write scaling is harder than read scaling. Writes involve: disk I/O, index updates, replication, consistency guarantees. Bursty high-throughput writes with contention are the hardest pattern to handle.

### Strategy 1: Vertical Scaling + Database Selection

- Optimize single server before distributing
- Choose the right DB for write patterns (e.g., Cassandra for write-heavy, Postgres for transactional)

### Strategy 2: Sharding and Partitioning

**Horizontal Sharding**
- Distribute data across multiple DB instances based on partition key
- Each shard handles a subset of rows
- Key selection is critical: bad keys = hot shards
- Resharding is a common interview follow-up ("How do you add more shards?")

**Vertical Partitioning**
- Split data by columns/features rather than rows
- Example: user profile in one DB, user activity logs in another
- Reduces per-write overhead on each partition

**Hot Key Problem**
- Some keys receive disproportionate writes (celebrity accounts, viral content)
- **Split All Keys**: distribute uniformly across more partitions
- **Split Hot Keys Dynamically**: runtime detection + redistribution of problematic keys to dedicated shards

### Strategy 3: Queues and Load Shedding

**Write Queues (Buffering)**
- Buffer incoming writes during traffic spikes
- Decouple write ingestion from write processing
- Queue absorbs burst; workers drain at sustainable rate
- Example: Kafka as write buffer -> workers process at DB's pace

**Load Shedding**
- Actively reject or defer requests when system capacity exceeded
- Return 429/503 rather than collapse the entire system
- Prioritize critical writes over non-critical ones

### Strategy 4: Batching and Hierarchical Aggregation

**Batching**
- Group multiple writes into single DB operation
- Reduces per-operation overhead (connection setup, index updates, disk flushes)
- Trade-off: increased latency for individual writes (wait for batch to fill or timer to fire)

**Hierarchical Aggregation**
- Multi-tier aggregation: local -> regional -> global
- Example: count likes locally, aggregate regionally, persist globally
- Reduces write amplification at each tier

### Interview Scenarios Using This Pattern
YouTube Top K, Strava, Rate Limiter, Ad Click Aggregator, FB Post Search, Metrics Monitoring

### Common Interview Probes
- "How do you handle resharding when you need to add more shards?"
- "What happens with hot keys?"
- "How do you handle write bursts without losing data?"

---

## 3. REAL-TIME UPDATES

**Source:** https://www.hellointerview.com/learn/system-design/deep-dives/realtime-updates and https://www.hellointerview.com/learn/system-design/patterns/realtime-updates

### The Core Problem

Standard HTTP request-response cannot support servers proactively pushing updates to clients. You need persistent, low-latency channels for: chat, collaborative editors, live dashboards, auctions, location tracking.

### Two-Hop Architecture

Real-time systems have two distinct communication paths:
- **Hop 1 (Server -> Client)**: delivering updates to connected clients
- **Hop 2 (Source -> Server)**: getting changes from origin to the delivery servers

### Client-Server Protocols (Hop 1)

#### Simple Polling
- Client sends HTTP requests at fixed intervals ("do you have updates?")
- Pros: simple, works through all firewalls, standard HTTP
- Cons: high latency (bounded by polling interval), wasteful (most responses empty), load scales linearly with clients
- Use when: low-frequency updates, latency tolerance exists

#### Long Polling
- Client sends request; server holds connection until data arrives or timeout
- Then client immediately reissues
- Pros: lower latency than simple polling, reduces empty responses
- Cons: connection churn (new connection per cycle), server maintains pending state, duplicate messages during reconnection
- Use when: need lower latency but can't use WebSockets/SSE

#### Server-Sent Events (SSE)
- Unidirectional push over HTTP. Server sends chunked responses with `text/event-stream` MIME type
- Uses HTTP long-lived connection with chunked transfer encoding
- Format: `data: {content}\n\n`
- Browser automatically reconnects with exponential backoff (uses `Last-Event-ID` header)
- **One direction only: server -> client**
- Pros: native browser support (`EventSource` API), auto-reconnection, simpler than WebSockets for one-way
- Cons: text only (no binary), server->client only, HTTP connection limits (browsers allow ~6 concurrent per domain), firewall/proxy edge cases
- Hello Interview note: "The amount of time we've spent dealing with networking edge cases is mind boggling" -- production complexity despite apparent simplicity

#### WebSockets
- Persistent TCP connection via HTTP upgrade handshake. **Full-duplex bidirectional.**
- Protocol flow:
  1. Client sends HTTP Upgrade request with `Upgrade: websocket` header
  2. Server responds with `101 Switching Protocols`
  3. Connection becomes bidirectional frame stream (not HTTP anymore)
- Frame overhead: **2-14 bytes** (vs HTTP headers ~500+ bytes)
- Frame opcodes: text=0x1, binary=0x2, close=0x8, ping=0x9, pong=0xA
- Pros: true bidirectional, minimal frame overhead, lowest latency, works through most firewalls
- Cons: more complex than SSE, requires application-level heartbeats, **stateful connections complicate horizontal scaling** (need sticky sessions), server crash drops ALL connected clients
- Scaling challenge: need sticky sessions or session affinity when distributing across servers

#### WebRTC
- Peer-to-peer via ICE (Interactive Connectivity Establishment) for NAT traversal
- Requires STUN/TURN infrastructure
- Pros: direct P2P (bypasses server), lowest possible latency
- Cons: complex setup, TURN relay expensive at scale, not suitable for fan-out
- Use when: P2P messaging, file transfer, direct endpoint communication

### Protocol Comparison

| Aspect | Simple Poll | Long Poll | SSE | WebSocket | WebRTC |
|--------|------------|-----------|-----|-----------|--------|
| Latency | High | Medium | Low | Very Low | Very Low |
| Bidirectional | No | No | No | **Yes** | Yes |
| Connection | Periodic | Persistent | Persistent | Persistent | Direct |
| Overhead/msg | ~500B header | ~500B header | Minimal | **2-14 bytes** | Variable |
| Setup | Trivial | Simple | Simple | Moderate | Complex |
| Server Load | High | Very High | Medium | Medium | Low |

### Server-Side Patterns (Hop 2)

#### Server-Side Polling
- Servers periodically query data sources for updates
- Same trade-offs as client polling (latency = polling interval, wasteful)

#### Consistent Hashing for Distribution
- Hash client IDs to server ring positions
- Determines which server "owns" a subscription
- Minimal redistribution when servers added/removed
- Trade-off: requires shared state or cross-server messaging

#### Pub/Sub Pattern
- **Publishers**: services generating updates (edits, orders, comments)
- **Subscribers**: real-time servers consuming from topics
- **Broker**: central system (Kafka, Redis Pub/Sub, RabbitMQ) managing routing
- Fan-out: each message sent to all subscribed servers
- At-least-once delivery (may duplicate)
- Ordered within topic/partition
- Key difference: **Redis Pub/Sub loses messages when no subscribers connected; Kafka retains configurable window**

### Connection Failure & Reconnection

- **Exponential backoff with jitter**: 1s -> 2s -> 4s -> 8s -> max 60s
- **Heartbeat/ping-pong**: detect dead connections before client notices
- **Sequence numbering**: track delivered messages; on reconnect, server resends gap
- **State sync**: on reconnect, client requests full state update
- Some systems accept losing messages (live comments, stock tickers) vs. guaranteed delivery (financial, chat)

### Fan-Out at Scale (Celebrity Problem)

Problem: single user with millions of followers all need the same update.

Solutions:
1. **Fan-out on write**: pre-compute and push to all followers' feeds on publish. Breaks at millions of followers.
2. **Fan-out on read**: store in single location; followers pull when viewing. Higher read latency.
3. **Hybrid**: fan-out for active users, on-read for inactive
4. **Hierarchical fan-out**: regional brokers subscribe to global topic, fan-out locally
5. **Lazy delivery**: notify "new items available"; followers pull on demand

### Message Ordering

- **Single partition per entity**: all updates for one doc/user go to one Kafka partition (preserves order). Bottleneck: throughput capped by single broker.
- **Vector clocks**: servers tag updates with causality info; clients reconstruct
- **Sequence numbers**: source assigns strictly increasing IDs; clients buffer out-of-order
- **Lamport timestamps**: logical timestamps for causally-related events

### When to Use Real-Time Updates
- Chat (messages <1s)
- Collaborative tools (doc edits, drawing)
- Live dashboards (metrics, stocks)
- Gaming (player positions)
- Live comments/feeds
- Location tracking (Uber, delivery)

### When NOT to Use
- Static content (HTTP caching)
- Low-frequency updates (polling sufficient)
- Best-effort acceptable (no ordering needed)
- Batch processing systems

### Interview Scenarios
Ticketmaster, Uber, WhatsApp, Robinhood, Google Docs, Strava, Online Auction, FB Live Comments

---

## 4. REDIS DEEP DIVE

**Source:** https://www.hellointerview.com/learn/system-design/deep-dives/redis

### What Redis IS

- **In-memory, single-threaded key-value data structure store** written in C
- Keys are always strings; values can be any supported data structure
- All data in RAM -> **microsecond read latency**, **~100K writes/second**
- Single-threaded -> simple to reason about, no race conditions within a single instance
- Trades **durability for speed** (unlike RDBMS with disk-based commit guarantees)

### Data Structures

**Strings**: binary-safe, store anything (text, JSON, serialized objects)
- SET, GET, INCR (atomic increment)

**Hashes**: field-value pairs (like a dict/object)
- Good for storing objects: `user:123 -> {name: "John", age: 30}`

**Lists**: ordered collections (linked list implementation)

**Sets**: unordered unique members
- SADD, SMEMBERS, SCARD, SISMEMBER
- Use: tracking unique visitors, tags, relationships

**Sorted Sets**: members ordered by score, **log-time operations**
- ZADD, ZRANGE, ZREMRANGEBYRANK
- Use: leaderboards, ranking, priority queues, top-K
- Example: `ZADD tiger_posts 500 "PostId1"` then `ZREMRANGEBYRANK tiger_posts 0 -6` (keep top 5)

**HyperLogLog**: probabilistic cardinality estimation
- Use: counting unique items with minimal memory (~12KB for billions of items)

**Bloom Filters**: probabilistic membership test
- Allows false positives, never false negatives
- Use: "has this user seen this content?"

**Geospatial Indexes**: longitude/latitude indexing
- GEOADD, GEOSEARCH (query radius around coordinates)
- Use: "find restaurants within 5km"

**Streams**: time-indexed ordered message queues
- XADD, XRANGE
- Can partially replace Kafka/SQS for simpler use cases

**Pub/Sub**: publish-subscribe messaging
- Fire-and-forget: **messages lost if no subscribers connected**
- Compare to Kafka which retains messages

### Clustering & Distribution

**Hash Slots Model**
- Clients cache mapping of hash slots -> nodes
- Keys hash to slots, slots map to nodes
- Clients connect directly to correct node (no proxy needed)
- **Critical**: Redis expects all data for a given request on a single node. Key structure determines scaling strategy.

**Gossip Protocol**: nodes maintain peer awareness; limited redirection if wrong node queried (MOVED response)

**Rebalancing**: during slot migration, servers respond with MOVED; clients refresh via `CLUSTER SHARDS`

**Configurations**:
- Single node (simplest)
- High-availability replica setup (primary + replicas)
- Multi-node cluster with rebalancing/failover

### Persistence

**Append-Only File (AOF)**: logs every write operation. Can replay to reconstruct state. Minimizes data loss but slower than RDB.

**RDB Snapshots**: point-in-time snapshots at intervals. Faster recovery but potential data loss between snapshots.

**Neither gives RDBMS-level guarantees.** For true durability, look at AWS MemoryDB (Redis-compatible with durability).

### Common Interview Patterns

#### 1. Caching
- Most common use case
- Key-value: `product:123` -> JSON blob or Hash
- TTL auto-evicts expired keys
- Does NOT solve hot key problem (single key getting disproportionate traffic)

#### 2. Distributed Locking
**Simple Timeout Lock (mechanical steps)**:
1. `INCR lock_key` (atomic)
2. If response = 1: you acquired the lock (first caller)
3. If response > 1: lock held by someone else; retry later
4. Set TTL on key (auto-release if holder crashes)
5. `DEL lock_key` when done (release for others)

**Advanced**: Redlock algorithm with fencing tokens for stronger guarantees

**Caveat**: "If your core database provides consistency, don't add distributed lock complexity." Interviewer will probe edge cases.

#### 3. Leaderboards (Sorted Sets)
- Sorted Sets maintain ordered data in log time
- High write throughput + low latency
- SQL struggles with this at scale (ORDER BY + LIMIT on large tables)

#### 4. Rate Limiting

**Fixed-Window Algorithm**:
1. On each request: `INCR user:123:requests`
2. If count > N: reject (rate limit exceeded)
3. If count <= N: allow
4. `EXPIRE` key after window W (e.g., 60 seconds)

**Sliding-Window Algorithm**:
- Store timestamps in Sorted Set
- Remove entries older than window
- Count remaining
- Run atomically via **Lua script** (critical for correctness)

#### 5. Proximity/Geo Search
- `GEOADD` to index locations
- `GEOSEARCH` to query radius

### Performance Numbers
- **~100K writes/second** baseline
- **Microsecond read latency**
- 100 sequential Redis requests = low overhead (viable, but batch if possible)

### Limitations
1. **No distributed transactions** across keys/nodes
2. **Hot key bottleneck** unsolved (single key = single node)
3. **Memory-bound**: entire dataset must fit in RAM (or use eviction policies)
4. **Single-threaded**: serializes all commands (simplifies reasoning but limits per-node throughput)
5. **Cluster is basic**: clients must solve scalability via key design

### When NOT to Use Redis
- Need strong durability guarantees (use RDBMS)
- Dataset too large for RAM
- Need complex queries (use SQL)
- Need distributed transactions

---

## 5. KAFKA DEEP DIVE

**Source:** https://www.hellointerview.com/learn/system-design/deep-dives/kafka

### What Kafka IS

- Open-source **distributed event streaming platform**
- Can function as **message queue** OR **stream processing system**
- Used by **80% of Fortune 100**
- Core abstraction: **distributed commit log** (append-only)

### Core Architecture

**Brokers**: individual servers in a Kafka cluster. Each hosts partitions.

**Topics**: logical grouping of partitions. Organize data logically. A topic can have multiple partitions distributed across brokers.

**Partitions**: ordered, immutable sequence of messages, continually appended to. Like a log file.
- Topics organize logically; **partitions scale physically**
- Each partition lives on one broker (leader) with replicas on other brokers

### Message Structure

Four fields:
- **Value**: the payload (the actual data)
- **Key**: determines partition assignment via hashing
- **Timestamp**: creation/ingestion time (ordering uses offsets, NOT timestamps)
- **Headers**: key-value metadata pairs

### How Partition Assignment Works (mechanical)

**Step 1 - Partition Determination**:
- Kafka hashes the message key -> assigns to specific partition
- **Messages with same key ALWAYS go to same partition** (preserves order per key)
- No key? Round-robin or "sticky" partitioner (batches to same partition for efficiency, then rotates)

**Step 2 - Broker Assignment**:
- Kafka controller maintains cluster metadata (partition -> broker mapping)
- Producers use this metadata to route directly to correct broker

### Append-Only Log Design

Three critical benefits:
1. **Immutability**: once written, messages cannot be altered in-place. Removed only via retention policies or log compaction.
2. **Efficiency**: append-only minimizes disk seek times (sequential I/O >> random I/O)
3. **Scalability**: simple mechanism enables horizontal scaling via partition distribution

### Offsets & Consumer Tracking

- Each message gets a **unique offset** (sequential position in partition)
- Consumers track progress by maintaining offsets
- Consumers **periodically commit offset back to Kafka**
- On crash: resume from last committed offset

**Delivery Semantics**:
- **At-least-once** (default): if consumer crashes after processing but before committing offset, message reprocessed on restart
- **Exactly-once**: requires idempotent producers + transactional APIs (more complex)

### Replication & Durability

**Leader-Follower Model**:
- Each partition has a **leader replica** on one broker
- Leader handles ALL writes and (by default) reads
- Followers replicate leader data for fault tolerance
- **ISR (In-Sync Replicas)**: followers that are caught up with leader

**acks configuration**:
- `acks=0`: no acknowledgment (fastest, least durable)
- `acks=1`: leader acknowledges (medium)
- `acks=all`: all ISR acknowledge (slowest, most durable)

### Consumer Groups

- Consumers form **consumer groups**
- Each partition assigned to **exactly one consumer** in the group
- Prevents duplicate processing while enabling parallelism
- Number of consumers <= number of partitions (extras sit idle)
- If consumer dies, its partitions reassigned to remaining consumers

### Message Queue vs Stream Mode

**Message Queue Mode**:
- Each message processed by one consumer in group, then effectively "consumed"
- Traditional queue semantics

**Stream Mode**:
- Log retained and can be replayed
- **Multiple consumer groups independently read same data**
- Consumers process continuously as data arrives
- Enables event sourcing, audit trails, reprocessing

### Partitioning Strategy

**Choosing the right key is CRITICAL**:
- Key determines which partition -> which consumer -> ordering guarantees
- Example: game_id as key ensures all events for one game go to one partition -> processed in order
- Bad key choice = out-of-order processing across partitions

**Sticky Partitioner** (modern default for null keys):
- Batches messages to same partition for efficiency
- Then rotates to next partition

### Log Compaction

- Alternative to time-based retention
- Keeps only the **latest value for each key**
- Use case: maintaining current state (like a changelog)
- Example: user profile updates -- only latest matters

### Key Interview Scenarios

1. **Ordering Guarantees**: only within partitions. Key selection determines ordering scope.
2. **Scalability**: horizontal via partition/broker distribution
3. **Durability**: replication + acks configuration
4. **Exactly-Once**: requires idempotent producers + transactions (ask about it, shows depth)
5. **Consumer Failure**: offset commits enable recovery; uncommitted = reprocess
6. **Backpressure**: consumers fall behind -> messages buffer in partitions (retained by retention policy)

### When to Use Kafka
- High-throughput event streaming (millions of events/sec)
- Decoupling producers from consumers
- Event sourcing / audit trails
- Stream processing pipelines
- Log aggregation
- Real-time data feeds

### When NOT to Use Kafka
- Simple request-response (use HTTP)
- Low-throughput messaging (use SQS or simple queues)
- Need strong ordering across ALL messages (only per-partition)
- Small team without ops capacity (operational complexity)

### Common Interview Problems Using Kafka
Ad Click Aggregator, FB Post Search, Metrics Monitoring, WhatsApp (message routing), YouTube Top K, Strava, News Aggregator

---

## CROSS-CUTTING INTERVIEW CHEAT SHEET

### "How do you scale reads?"
1. Indexing -> 2. Read replicas -> 3. Cache (Redis) -> 4. CDN

### "How do you scale writes?"
1. Optimize DB choice -> 2. Shard/partition -> 3. Queue writes (Kafka) -> 4. Batch + aggregate

### "How do you do real-time?"
1. Determine latency requirement
2. Pick protocol: polling (>5s ok) / SSE (server->client) / WebSocket (bidirectional)
3. Server side: Pub/Sub (Kafka or Redis) for source->server
4. Address: reconnection, ordering, fan-out

### "Tell me about Redis"
In-memory data structure store. ~100K writes/sec, microsecond reads. Use for: cache, distributed locks, leaderboards, rate limiting, geo search. NOT for: durability, complex queries, huge datasets.

### "Tell me about Kafka"
Distributed commit log. Use for: high-throughput event streaming, decoupling, event sourcing, stream processing. Key concepts: topics/partitions, consumer groups, offsets, at-least-once default. NOT for: simple request-response, low-volume messaging.
