# Pix Transaction Processing — Solução

## Requirements
- **Func:** Validar saldo → debitar remetente → creditar destinatário → registrar extrato → notificar
- **Non-Func:** 5M Pix/dia, SLA 10s ponta a ponta, consistência forte na transação
- **Consistência > disponibilidade** (dinheiro não pode sumir)

## Napkin Math
```
Write: 5M/dia ÷ 86.4K = 57 QPS → peak ~170 QPS
Volume BAIXO → Postgres single instance resolve
Lock contention: 57 QPS / 5M users = praticamente zero colisão
Storage: 5M × 1KB × 365 = ~1.8TB/ano
```

## Decisão Arquitetural Chave
```
57 QPS + ambas contas no mesmo banco = TRANSAÇÃO ACID SIMPLES
NÃO precisa de Saga. NÃO precisa de Kafka pro core.
Saga = quando dados estão em bancos/serviços DIFERENTES.
```

## Core Entities
```
Account {
    account_id:  UUID (PK)
    user_id:     string (FK)
    balance:     decimal
    currency:    string
    updated_at:  datetime
}

Transaction {
    transaction_id:  UUID (PK)
    sender_id:       string (FK)
    receiver_id:     string (FK)
    amount:          decimal
    status:          enum (PENDING, COMPLETED, FAILED)
    created_at:      datetime
}

TransactionOutbox {
    event_id:        UUID (PK)
    transaction_id:  string (FK)
    event_type:      enum (COMPLETED, FAILED)
    published:       boolean (default false)
    created_at:      datetime
}
```

## Arquitetura

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         CORE: TRANSAÇÃO ATÔMICA                              │
│                                                                              │
│  ┌─────────┐    ┌─────────┐    ┌──────────┐    ┌──────────────────┐          │
│  │  App    │───▶│ API GW  │───▶│   LB     │───▶│   Pix Service    │         │
│  │ (user)  │    │         │    │          │    │                  │          │
│  └─────────┘    └─────────┘    └──────────┘    └────────┬─────────┘          │
│                                                         │                    │
│                                              ┌──────────▼───────────┐        │
│                                              │  POSTGRES (1 tx)     │        │
│                                              │                      │        │
│                                              │  BEGIN;               │        │
│                                              │                      │        │
│                                              │  -- validar saldo    │        │
│                                              │  SELECT balance      │        │
│                                              │  FROM accounts       │        │
│                                              │  WHERE user_id =     │        │
│                                              │    sender            │        │
│                                              │  FOR UPDATE;         │        │
│                                              │                      │        │
│                                              │  -- debitar          │        │
│                                              │  UPDATE accounts     │        │
│                                              │  SET balance =       │        │
│                                              │    balance - 50      │        │
│                                              │  WHERE user_id =     │        │
│                                              │    sender;           │        │
│                                              │                      │        │
│                                              │  -- creditar         │        │
│                                              │  UPDATE accounts     │        │
│                                              │  SET balance =       │        │
│                                              │    balance + 50      │        │
│                                              │  WHERE user_id =     │        │
│                                              │    receiver;         │        │
│                                              │                      │        │
│                                              │  -- registrar tx     │        │
│                                              │  INSERT transaction  │        │
│                                              │                      │        │
│                                              │  -- outbox event     │        │
│                                              │  INSERT outbox       │        │
│                                              │                      │        │
│                                              │  COMMIT;             │        │
│                                              │                      │        │
│                                              │  ← TUDO ATÔMICO →   │        │
│                                              └──────────────────────┘        │
│                                                                              │
│  Se falhar em qualquer ponto → ROLLBACK automático                           │
│  Nenhum dinheiro some. Nenhum dinheiro duplica.                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                    ASYNC: EXTRATO + NOTIFICAÇÃO                              │
│                                                                              │
│  ┌──────────────────┐    ┌──────────────────┐    ┌────────────────────────┐  │
│  │  Outbox Poller    │───▶│  Kafka (tópico   │───▶│  Consumers             │  │
│  │  (lê outbox,     │    │   extrato)       │    │                        │  │
│  │   publica,       │    │  partition:       │    │  Consumer Extrato:     │  │
│  │   marca done)    │    │   user_id        │    │   → DynamoDB (feed)    │  │
│  └──────────────────┘    └──────────────────┘    │                        │  │
│                                                   │  Consumer Notificação: │  │
│                                                   │   → Push/SMS sender   │  │
│                                                   │   → Push/SMS receiver │  │
│                                                   │                        │  │
│                                                   │  Se falha → DLQ        │  │
│                                                   └────────────────────────┘  │
│                                                                              │
│  ← Reusa a arquitetura do Problema 1 (Event Feed) →                         │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│              ALTERNATIVA NUBANK: DATOMIC (append-only)                        │
│                                                                              │
│  Ao invés de UPDATE balance, APPEND novo fato:                               │
│                                                                              │
│  {:user "sender",   :amount -50, :tx-id "abc", :time "2026-03-03T20:00"}    │
│  {:user "receiver", :amount +50, :tx-id "abc", :time "2026-03-03T20:00"}    │
│                                                                              │
│  Saldo atual = SUM(amount) WHERE user = X                                    │
│  Auditoria total. Nunca perde dado. Imutável.                                │
│  Transação ACID continua valendo no Datomic.                                 │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Deep Dives

### Por que NÃO Saga?
- Saga = múltiplos serviços, cada um com seu banco, sem transação compartilhada
- Aqui: sender e receiver no MESMO Postgres/Datomic → ACID resolve
- Saga traria complexidade de compensação desnecessária pra 57 QPS
- **Se no futuro contas ficarem em bancos diferentes (multi-região)**, aí sim Saga

### Lock e Contention
- FOR UPDATE faz lock pessimista no row do sender
- Com 57 QPS distribuído entre milhões de users, colisão é praticamente zero
- Lock dura microsegundos (tempo do UPDATE)
- Se escalar pra milhares de QPS na mesma conta (lojista), considerar OCC

### Double-spend Prevention
- Transação ACID já previne: se balance < amount, SELECT falha → ROLLBACK
- Idempotency key: transaction_id como UUID gerado pelo client → se request duplica, mesmo tx_id não processa 2x

## Trade-offs
1. **ACID simples vs Saga**: aceito acoplamento no mesmo DB, ganho simplicidade e garantia atômica. Se escalar pra multi-banco, rearquiteto.
2. **Mutar saldo (Postgres) vs Append-only (Datomic)**: se Postgres, aceito perder auditoria nativa mas ganho simplicidade. Nubank prefere append-only.

## Melhoria com mais tempo
- Reconciliação batch: job diário que valida SUM(débitos) = SUM(créditos)
- Circuit breaker no serviço do Banco Central (comunicação externa)
- Rate limiting por conta (prevenir abuso)
