                                      ┌─────────────────────────┐
                                      │         CLIENT          │
                                      │   mobile / POS / web    │
                                      └─────────────┬───────────┘
                                                    │
                                                    ▼
                                      ┌─────────────────────────┐
                                      │       API GATEWAY       │
                                      │ auth / rate limiting    │
                                      └─────────────┬───────────┘
                                                    │
                                                    ▼
                                      ┌─────────────────────────┐
                                      │     PAYMENT SERVICE     │
                                      │ create transaction      │
                                      └─────────────┬───────────┘
                                                    │
                                                    ▼
                                      ┌─────────────────────────┐
                                      │     CIRCUIT BREAKER     │
                                      │ timeout / retries       │
                                      └─────────────┬───────────┘
                                                    │
                     ┌──────────────────────────────┼─────────────────────────────┐
                     │                              │                             │
                     ▼                              ▼                             ▼
          ┌───────────────────┐        ┌───────────────────┐         ┌───────────────────┐
          │   FRAUD SERVICE   │        │   FRAUD SERVICE   │         │   FRAUD SERVICE   │
          │    instance 1     │        │    instance 2     │         │    instance 3     │
          │                   │        │                   │         │                   │
          │ feature builder   │        │ feature builder   │         │ feature builder   │
          │ model scoring     │        │ model scoring     │         │ model scoring     │
          │ decision engine   │        │ decision engine   │         │ decision engine   │
          └─────────┬─────────┘        └─────────┬─────────┘         └─────────┬─────────┘
                    │                            │                             │
                    └───────────────┬────────────┴─────────────┬───────────────┘
                                    │                          │
                                    ▼                          ▼
                           ┌─────────────────────────────────────────┐
                           │               REDIS CLUSTER             │
                           │                                         │
                           │   shard1        shard2        shard3    │
                           │ user feats      card feats     merchant │
                           │                                         │
                           │  primary + replicas (HA failover)       │
                           └───────────────┬─────────────────────────┘
                                           │
                                           ▼
                             ┌─────────────────────────┐
                             │   FRAUD DECISION        │
                             │ APPROVE / BLOCK / REVIEW│
                             └─────────────┬───────────┘
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    │                                             │
                    ▼                                             ▼
          ┌──────────────────────┐                     ┌──────────────────────┐
          │   PAYMENT PROCESSOR  │                     │      FALLBACK        │
          │ (Visa / Mastercard)  │                     │   fail-open approve  │
          │                      │                     │   if service down    │
          └─────────────┬────────┘                     └─────────────┬────────┘
                        │                                           │
                        ▼                                           ▼
                ┌──────────────────────┐                   ┌──────────────────────┐
                │      TRANSACTION     │                   │      MONITORING      │
                │       RESULT         │                   │ alerts / metrics     │
                └─────────────┬────────┘                   └──────────────────────┘
                              │
                              ▼
                     ┌──────────────────────┐
                     │         KAFKA        │
                     │ topic: transactions  │
                     └─────────────┬────────┘
                                   │
                                   ▼
                    ┌───────────────────────────────────┐
                    │             FLINK                 │
                    │                                   │
                    │ stream processing                 │
                    │ velocity detection                │
                    │ real-time aggregations            │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                           ┌──────────────────────┐
                           │      DATA LAKE       │
                           │ transactions history │
                           └─────────────┬────────┘
                                         │
                                         ▼
                           ┌──────────────────────┐
                           │     ML TRAINING      │
                           │ Spark / batch jobs   │
                           └─────────────┬────────┘
                                         │
                                         ▼
                           ┌──────────────────────┐
                           │     MODEL REGISTRY   │
                           │ versioned models     │
                           └─────────────┬────────┘
                                         │
                                         ▼
                        ┌────────────────────────────────┐
                        │   FRAUD SERVICE MODEL UPDATE   │
                        │ rolling deployment / A/B test  │
                        └────────────────────────────────┘