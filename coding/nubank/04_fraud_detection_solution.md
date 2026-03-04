# Fraud Detection Pipeline — Solução

## Requirements
- **Func:** Toda transação recebe score de risco (0-100). Baixo: passa. Médio: confirma com user. Alto: bloqueia + analista.
- **Non-Func:** 450M events/dia, latência <100ms, disponibilidade > consistência
- **Disponibilidade é prioridade** — se anti-fraude cai, remove proteção do banco e dos usuários

## Napkin Math
```
Write: 450M/dia ÷ 86.4K = 5.2K QPS → peak ~15K QPS
Kafka: 1M msg/s capacity → 15K é tranquilo
Flink: precisa processar 5.2K events/s com lookup de features
Redis: 5.2K lookups/s (features) → trivial (100K ops/s capacity)
Model inference: <50ms (SLA 100ms total, sobra 50ms pra rede+lookup)
```

## Core Entities
```
Transaction Event (Kafka) {
    transaction_id:  UUID
    user_id:         string
    type:            enum (PIX, CARD, BILL)
    amount:          decimal
    receiver_id:     string
    merchant:        string (nullable)
    location:        string
    timestamp:       datetime
}

Fraud Score Output (Kafka) {
    transaction_id:  UUID
    user_id:         string
    score:           float (0-100)
    action:          enum (ALLOW, CONFIRM, BLOCK)
    features_used:   json
    model_version:   string
    timestamp:       datetime
}

User Features (Redis) {
    key: "features:{user_id}"
    avg_transaction_30d:     decimal
    tx_count_30d:            int
    common_merchants:        list
    common_locations:        list
    max_single_tx_90d:       decimal
    account_age_days:        int
    ttl: 24h (refreshed daily by batch)
}
```

## Arquitetura

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                     FEATURE STORE (2 camadas)                                │
│                                                                              │
│  ┌─── OFFLINE (batch, diário) ──────────────────────────────────────────┐    │
│  │                                                                      │    │
│  │  Datomic/S3 ──→ Spark job ──→ Calcula features ──→ Redis            │    │
│  │  (histórico      (diário)     (médias 30/90d,       (features       │    │
│  │   transações)                  padrões user)         prontas,       │    │
│  │                                                      TTL 24h)       │    │
│  └──────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─── ONLINE (real-time, Flink) ───────────────────────────────────────┐    │
│  │                                                                      │    │
│  │  Flink calcula em janela de tempo:                                   │    │
│  │  - Quantos Pix nos últimos 5 min?                                    │    │
│  │  - Valor acumulado última 1h?                                        │    │
│  │  - Destinatário novo? (nunca recebeu antes)                          │    │
│  │  - Localização diferente da usual?                                   │    │
│  │                                                                      │    │
│  └──────────────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                     SCORING PIPELINE                                         │
│                                                                              │
│  ┌──────────────┐    ┌──────────────────────────────────────────────────┐    │
│  │ Pix/Card/    │    │              FLINK                               │    │
│  │ Bill Service │    │                                                  │    │
│  │  (producers) │    │  1. Recebe evento do Kafka                       │    │
│  └──────┬───────┘    │  2. Calcula features real-time (janela 5min/1h)  │    │
│         │            │  3. Busca features históricas no Redis (<1ms)    │    │
│         ▼            │  4. Monta feature vector completo                │    │
│  ┌──────────────┐    │  5. Chama Model Service (inference <50ms)       │    │
│  │    KAFKA     │───▶│  6. Score → decisão (ALLOW/CONFIRM/BLOCK)       │    │
│  │  tópico:     │    │  7. Publica resultado no Kafka                  │    │
│  │  transactions│    │                                                  │    │
│  │  partition:  │    └──────────────────────┬───────────────────────────┘    │
│  │  user_id     │                           │                                │
│  │  128 parts   │                           ▼                                │
│  └──────────────┘    ┌──────────────────────────────────────────────────┐    │
│                      │    KAFKA — tópico: fraud-alerts                  │    │
│                      │    (score + action por transação)                │    │
│                      └──────────────┬──────────────┬───────────────────┘    │
│                                     │              │                         │
│                                     ▼              ▼                         │
│                      ┌──────────────────┐  ┌──────────────────┐             │
│                      │  Action Consumer  │  │  Audit Consumer  │             │
│                      │                   │  │                  │             │
│                      │  ALLOW → libera   │  │  Grava TODOS os  │             │
│                      │  CONFIRM → push   │  │  scores no S3    │             │
│                      │    pro user       │  │  (auditoria,     │             │
│                      │  BLOCK → bloqueia │  │   retrain)       │             │
│                      │    + envia pra    │  │                  │             │
│                      │    analista       │  └──────────────────┘             │
│                      └──────────────────┘                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                     MODEL SERVICE                                            │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐    │
│  │                    Load Balancer                                      │    │
│  │                         │                                             │    │
│  │         ┌───────────────┼───────────────┐                             │    │
│  │         ▼               ▼               ▼                             │    │
│  │  ┌───────────┐   ┌───────────┐   ┌───────────┐                       │    │
│  │  │ Container │   │ Container │   │ Container │   Auto-scaling        │    │
│  │  │ (model    │   │ (model    │   │ (model    │   Multi-region        │    │
│  │  │  v2.3)    │   │  v2.3)    │   │  v2.3)    │   Inference <50ms    │    │
│  │  └───────────┘   └───────────┘   └───────────┘                       │    │
│  │                                                                       │    │
│  │  Circuit Breaker: se modelo não responde em 80ms                      │    │
│  │  → Fallback: RULES ENGINE                                             │    │
│  │    - valor > R$10K → BLOCK                                            │    │
│  │    - destinatário novo + valor > R$2K → CONFIRM                       │    │
│  │    - horário/valor normal → ALLOW                                     │    │
│  │    (pior que modelo, melhor que nada)                                  │    │
│  └──────────────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Deep Dives

### Features em 2 Camadas
- **Históricas (Redis):** pré-computadas pelo Spark diariamente. Média 30d, padrões, merchants. Lookup <1ms.
- **Real-time (Flink):** calculadas na hora. Janela 5min/1h. "Quantos Pix nos últimos 5 min?"
- **Por que 2 camadas?** Features históricas mudam devagar (batch ok). Features real-time precisam ser frescas (stream).

### Circuit Breaker + Graceful Degradation
- Model Service cai → Circuit Breaker abre → Rules Engine assume
- Rules Engine: conjunto de IF/ELSE simples, sem ML
- Não é tão bom quanto o modelo, mas protege o banco
- Quando Model Service volta → Circuit Breaker fecha → volta pro modelo

### Métricas
- **Recall** é a prioridade: "de todas as fraudes, quantas o modelo pegou?"
- Melhor bloquear legítimo (falso positivo) do que deixar fraude passar (falso negativo)
- Threshold de score ajustável: abaixar = mais bloqueios, mais seguro, mais atrito

### Model Update
- Novo modelo treinado → deploy em canary (10% tráfego)
- Se métricas ok → rollout 100%
- Se métricas caem → rollback automático pro modelo anterior

## Trade-offs
1. **Flink na stack**: ganho processamento real-time com baixa latência, aceito complexidade operacional (sistema distribuído, time precisa saber operar)
2. **Redis pra features**: ganho lookup sub-ms, preciso gerenciar TTL e storage. Redis cluster pra alta disponibilidade.
3. **Recall > Precision**: aceito falsos positivos (bloqueio legítimo) pra minimizar fraude real. Trade-off de negócio.

## Melhoria com mais tempo
- Flink como plataforma compartilhada (anti-fraude, anti-lavagem, compliance, real-time analytics)
- A/B test de modelos em produção (canary deployment)
- Feedback loop: analista confirma/nega → dado volta pro training set
