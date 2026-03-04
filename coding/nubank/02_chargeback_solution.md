# Chargeback / Dispute System — Solução

## Requirements
- **Func:** Cliente contesta cobrança pelo app → crédito temporário → investigação (auto + manual) → aprovado ou negado
- **Non-Func:** 40M DAU, 40K chargebacks/dia, disputa dura 7-90 dias
- **Consistência forte** (dados financeiros, não pode perder disputa)

## Napkin Math
```
Write: 40K/dia ÷ 86.4K = 0.46 QPS → peak ~1.4 QPS
Read (analista + usuário): ~10x write = ~5 QPS peak
Volume MUITO baixo → Postgres single instance resolve tudo
Storage: 40K × 2KB × 365 = ~30GB/ano (trivial)
```

## Core Entities
```
Chargeback {
    chargeback_id:   UUID (PK)
    user_id:         string (FK)
    transaction_id:  string (FK, transação original contestada)
    amount:          decimal
    reason:          string
    state:           enum (OPENED, AUTO_REVIEW, MANUAL_REVIEW, APPROVED, DENIED)
    created_at:      datetime
    updated_at:      datetime
    resolved_at:     datetime (nullable)
    resolved_by:     string (nullable — "SYSTEM" ou analyst_id)
}

ChargebackEvent (Outbox) {
    event_id:        UUID (PK)
    chargeback_id:   string (FK)
    event_type:      enum (OPENED, STATE_CHANGED, RESOLVED)
    payload:         json
    published:       boolean (default false)
    created_at:      datetime
}
```

## State Machine
```
                    ┌──────────── APPROVED ──→ crédito definitivo
                    │
OPENED ──→ AUTO_REVIEW ──→ MANUAL_REVIEW ──→ APPROVED ──→ crédito definitivo
  │                │              │
  │                │              └──→ DENIED ──→ estorno crédito temporário
  │                │
  │                └──────────── DENIED ──→ estorno crédito temporário
  │
  └──→ (ação paralela: liberar crédito temporário)
```

## Arquitetura

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         ABERTURA DO CHARGEBACK                               │
│                                                                              │
│  ┌─────────┐    ┌─────────┐    ┌──────────┐    ┌──────────────────┐          │
│  │  App    │───▶│ API GW  │───▶│   LB     │───▶│ Chargeback Svc   │         │
│  │ (user)  │    │         │    │          │    │                  │          │
│  └─────────┘    └─────────┘    └──────────┘    └────────┬─────────┘          │
│                                                         │                    │
│                                              ┌──────────▼───────────┐        │
│                                              │   POSTGRES (1 tx)    │        │
│                                              │                      │        │
│                                              │  INSERT chargeback   │        │
│                                              │  (state: OPENED)     │        │
│                                              │         +            │        │
│                                              │  INSERT outbox event │        │
│                                              │  (published: false)  │        │
│                                              │                      │        │
│                                              │  ← MESMA TRANSAÇÃO → │        │
│                                              │    (Outbox Pattern)  │        │
│                                              └──────────────────────┘        │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                         OUTBOX → FILA → PROCESSAMENTO                        │
│                                                                              │
│  ┌──────────────────┐    ┌──────────────────┐    ┌────────────────────────┐  │
│  │  Outbox Poller    │───▶│  Chargeback Queue │───▶│  Chargeback Consumer  │  │
│  │  (lê outbox table │    │  (SQS ou Kafka)   │    │                      │  │
│  │   a cada 5s,      │    │                   │    │  Recebe evento:      │  │
│  │   publica na fila,│    │                   │    │                      │  │
│  │   marca published │    │                   │    │  OPENED:             │  │
│  │   = true)         │    │                   │    │   → Credit Svc:      │  │
│  └──────────────────┘    └───────────────────┘    │     libera temp      │  │
│                                                    │   → state→AUTO_REVIEW│  │
│                                                    │                      │  │
│                                                    │  AUTO_REVIEW:        │  │
│                                                    │   → Rules/ML check   │  │
│                                                    │   → resolve?         │  │
│                                                    │     SIM → APPROVED   │  │
│                                                    │           ou DENIED  │  │
│                                                    │     NÃO → MANUAL     │  │
│                                                    │                      │  │
│                                                    │  MANUAL resolved:    │  │
│                                                    │   → APPROVED:        │  │
│                                                    │     Credit Svc:      │  │
│                                                    │     definitivo       │  │
│                                                    │   → DENIED:          │  │
│                                                    │     Credit Svc:      │  │
│                                                    │     estorno temp     │  │
│                                                    │                      │  │
│                                                    │  Falha → DLQ         │  │
│                                                    └──────────────────────┘  │
│                                                                              │
│  ┌──────────────┐                                                            │
│  │     DLQ      │  msgs que falharam 3x → alerta → retry manual             │
│  └──────────────┘                                                            │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                         TELA DO ANALISTA                                     │
│                                                                              │
│  ┌──────────────┐    ┌─────────┐    ┌──────────┐    ┌──────────────────┐     │
│  │ Admin Page   │───▶│ API GW  │───▶│   LB     │───▶│ Chargeback Svc   │    │
│  │ (analista)   │    │         │    │          │    │                  │     │
│  └──────────────┘    └─────────┘    └──────────┘    └────────┬─────────┘     │
│                                                              │               │
│  GET /chargebacks?state=MANUAL_REVIEW                        │               │
│  → lista chargebacks pendentes de análise                    │               │
│                                                              │               │
│  POST /chargebacks/:id/resolve {decision: APPROVED/DENIED}   │               │
│  → Postgres: update state + insert outbox event              │               │
│  → Outbox Poller publica na fila                             │               │
│  → Consumer executa crédito/estorno                          │               │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                         SERVIÇOS EXTERNOS                                    │
│                                                                              │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐        │
│  │  Credit Service   │    │ Notification Svc  │    │  Card Network    │       │
│  │                   │    │                   │    │  (Visa/Master)   │       │
│  │ - temp credit     │    │ - push/email user │    │  - consulta      │       │
│  │ - definitive      │    │   a cada mudança  │    │    lojista       │       │
│  │ - estorno         │    │   de estado       │    │  - (async, pode  │       │
│  │                   │    │                   │    │    demorar dias) │       │
│  └──────────────────┘    └──────────────────┘    └──────────────────┘        │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Deep Dives

### Outbox Pattern (evita dual write)
- Problema: preciso gravar no Postgres E publicar na fila. Se um falha, inconsistência.
- Solução: gravo chargeback + evento na **mesma transação** do Postgres.
- Poller separado lê eventos não publicados e envia pra fila.
- Se poller falha, eventos ficam no Postgres → nada se perde.

### Idempotência
- Consumer recebe mesmo evento 2x → checa estado atual no Postgres
- Se já está em AUTO_REVIEW, ignora evento OPENED duplicado
- Credit Service: chave idempotente = chargeback_id + tipo_credito

### Timeout
- Chargeback aberto há >90 dias sem resolução → job scheduled fecha como DENIED
- Analista sem ação em 7 dias → escala pra supervisor (SLA)

### Audit Trail
- Tabela chargeback_history: toda mudança de estado é registrada
- Quem mudou, quando, de qual estado pra qual (append-only, imutável)
- Nubank DNA: dados financeiros nunca são deletados

## Trade-offs
1. **Async (fila) vs sync (API call direto)**: aceito delay de segundos na execução do crédito, ganho resiliência — se Credit Svc cai, evento espera na fila
2. **Postgres vs DynamoDB**: volume é 0.46 QPS, Postgres dá ACID nativo pra transação do Outbox, sem necessidade de escala horizontal
3. **Auto + Manual review**: invisto em complexidade do fluxo, mas reduzo carga dos analistas (~70% dos casos simples resolvidos automaticamente)

## Melhoria com mais tempo
- Notificação push/email pro usuário a cada mudança de estado
- Dashboard de métricas: tempo médio de resolução, % auto vs manual, taxa de aprovação
- Circuit breaker no Credit Service (se cair, consumer para de tentar e acumula na fila)
