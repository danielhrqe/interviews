| | O que fazer |
|-|------------|
| **Colaboração** | Voz alta. Perguntar. "What do you think?" |
| **Arquitetura** | Classes pequenas. 1 método = 1 propósito |
| **Problem Solving** | Clarifying Qs → simples → adapta follow-up |
| **Code Quality** | Nomes claros, SOLID, DRY, testável |

| Problema | Core | Follow-ups |
|----------|------|------------|
| **Circuit Breaker** ⭐ | 3 estados (CLOSED→OPEN→HALF_OPEN), time window, dict por serviço | Config por serviço, thread safety, fallback |
| **Currency Converter** ⭐ | Account+Exchange, rates HashMap, fee por par | Rota indireta (2 hops), rate expiration |
| **Simple Cache** | get/put + TTL + LRU eviction (min by last_access) | Max size, thread safety |
| **Rate Limiter** | Contador + janela tempo, allow→increment→reset | Sliding window, por endpoint |
| **Tic-Tac-Toe** | Board(NxN) + Player + Game, check rows/cols/diags | NxN, undo (history list) |

## Cola Rápida

```
CIRCUIT BREAKER:
CLOSED ──3 fails/10min──→ OPEN ──5min──→ HALF_OPEN ──ok?──→ CLOSED
                                                    ──fail?→ OPEN

CURRENCY:
Direct:   BRL ─rate+fee─→ USD
Indirect: BRL ─rate+fee─→ USD ─rate+fee─→ NGN

CACHE:    get(key) → check TTL → hit/miss. put() → full? → evict min(last_access)
RATE:     allow(key) → new? create. expired? reset. over limit? block. else increment.
```
## Frases

- **Abrir:** "Let me make sure I understand the requirements."
- **Pensando:** "I'm using a dict here for O(1) lookup."
- **Trade-off:** "Let me get core logic right first, then we discuss concurrency."
- **Follow-up:** "Good question. Let me refactor to support that."
- **Dinheiro:** "In production I'd use Decimal for precision."
- **Não sabe:** "Not sure about syntax, but the idea is..."