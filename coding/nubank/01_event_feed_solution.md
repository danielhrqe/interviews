# Event Feed (Extrato Bancário) — Solução

## Requirements
- **Func:** Usuário abre app e vê extrato (Pix, cartão, boleto, estorno) em ordem cronológica
- **Non-Func:** 70M users, 40M DAU, 1B events/dia, leitura <200ms, paginação 20-30 items
- **Saldo:** strong consistency | **Feed:** eventual consistency (2-3s delay ok)
- **Disponibilidade** prioridade pro feed

## Napkin Math
```
Write: 1B/dia ÷ 100K = 10K QPS → peak 30K QPS (precisa Kafka)
Read:  40M DAU × 3.5 aberturas ÷ 100K = 1.4K QPS → peak ~5K QPS (DynamoDB tranquilo)
Msg size: ~0.5KB
Storage/ano: 1B × 0.5KB × 365 = ~180TB
```

## Core Entities
```
Event {
    event_id:       UUID (PK)
    user_id:        string (partition key)
    type:           enum (PIX_SENT, PIX_RECEIVED, CARD_PURCHASE, BILL_PAID, REFUND)
    amount:         decimal
    description:    string
    counterpart:    string (nome da outra parte)
    timestamp:      datetime (sort key)
    metadata:       json
}
```

## Arquitetura

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                              WRITE PATH                                      │
│                                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                                   │
│  │ Pix Svc  │  │ Card Svc │  │ Bill Svc │   (producers — publicam após      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘    transação concluída)           │
│       │              │             │                                          │
│       └──────────────┼─────────────┘                                         │
│                      ▼                                                       │
│  ┌──────────────────────────────────────────┐                                │
│  │          KAFKA — tópico: extrato          │                                │
│  │  partition key: user_id                   │                                │
│  │  ~100 partições                           │                                │
│  │  garante ordem por usuário                │                                │
│  │  replicação: 3 brokers                    │                                │
│  └──────────────────┬───────────────────────┘                                │
│                     ▼                                                        │
│  ┌──────────────────────────────────────────┐                                │
│  │        CONSUMER GROUP (extrato)           │                                │
│  │  - Lê evento do Kafka                     │                                │
│  │  - Checa idempotência (user_id +          │                                │
│  │    event_id no DynamoDB)                  │                                │
│  │  - Persiste no DynamoDB                   │                                │
│  │  - Se falha → DLQ (3 retries)             │                                │
│  └──────────┬──────────────┬────────────────┘                                │
│             │              │                                                 │
│             ▼              ▼                                                 │
│  ┌──────────────┐  ┌──────────────┐                                          │
│  │   DynamoDB    │  │ Notification │                                          │
│  │  PK: user_id  │  │   Service    │                                          │
│  │  SK: timestamp │  │ (async, se   │                                          │
│  │  (extrato)    │  │  falhar, ok) │                                          │
│  └──────────────┘  └──────────────┘                                          │
│                                                                              │
│  ┌──────────────┐                                                            │
│  │     DLQ      │  msgs que falharam 3x → alerta → retry manual             │
│  └──────────────┘                                                            │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                              READ PATH                                       │
│                                                                              │
│  ┌─────────┐    ┌─────────┐    ┌──────────┐    ┌──────────────┐              │
│  │  App    │───▶│ API GW  │───▶│   LB     │───▶│  Extrato Svc │             │
│  │ (user)  │    │         │    │          │    │              │              │
│  └─────────┘    └─────────┘    └──────────┘    └──────┬───────┘              │
│                                                       │                      │
│                                              Query: user_id = X              │
│                                              ScanIndexForward: false          │
│                                              Limit: 20                        │
│                                              ExclusiveStartKey: cursor        │
│                                                       │                      │
│                                                       ▼                      │
│                                                ┌──────────────┐              │
│                                                │   DynamoDB    │              │
│                                                │  (eventual    │              │
│                                                │   consistency │              │
│                                                │   read)       │              │
│                                                └──────────────┘              │
│                                                                              │
│  Paginação: cursor-based (LastEvaluatedKey do DynamoDB)                      │
│  Latência: <200ms (DynamoDB single-digit ms + rede)                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Deep Dives

### Idempotência
- DynamoDB: PK=user_id, SK=event_id → put idempotente (mesma chave sobrescreve)
- Consumer processa mesmo evento 2x → sem duplicação no extrato

### Ordenação
- Kafka: partition key = user_id → ordem garantida por usuário dentro da partição
- DynamoDB: sort key = timestamp → query retorna ordenado

### Falhas
- Consumer falha → mensagem não é commitada → Kafka re-entrega
- Após 3 retries → DLQ → alerta → investigação manual
- Notificação falha → extrato já está persistido, usuário faz refresh

### Escalabilidade
- Write: Kafka escala com partições + brokers
- Read: DynamoDB auto-scaling (on-demand mode)
- Consumer: escala até N = número de partições

## Trade-offs
1. **Eventual consistency no feed** (vs strong): aceito 2-3s delay em troca de alta disponibilidade e arquitetura mais simples
2. **DynamoDB vs Postgres**: aceito vendor lock-in AWS em troca de auto-scaling e latência single-digit ms sem tuning
3. **Tópico único vs múltiplos**: perco flexibilidade de processar tipos diferentes em velocidades diferentes, ganho ordenação garantida

## Melhoria com mais tempo
- Push notification pro usuário quando novo evento chega no extrato
- Cache Redis dos últimos 20 eventos pra reads frequentes (hot path)
