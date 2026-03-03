# Wise Pair Programming — Problemas Reportados

> Entrevista: 3/mar 08:30 BRT | Engineering Lead | HackerRank CodePair | 1h
> Formato: problema base → resolve → entrevistador MUDA requisitos → adapta
> Linguagem: Python (confirmar com recruiter — default é Java)
> NÃO é DSA/LeetCode. Foco: OOP, clean code, design patterns, colaboração.

## 4 Dimensões Avaliadas

1. **Colaboração** — pensa em voz alta, pede ajuda, incorpora feedback
2. **Arquitetura** — decisões de design, OOP, trade-offs
3. **Problem Solving** — abordagem, adaptação quando requisitos mudam
4. **Code Quality** — clean, testável, SOLID, DRY, KISS

## Problemas por Prioridade

### P1: Circuit Breaker ⭐ (MAIS REPORTADO)
- **Arquivo:** `01_circuit_breaker.py` ✅ FEITO
- **Cenário:** WebClient chama bancos parceiros. Banco cai, requests continuam, cascade failure.
- **O que constrói:** proteção com 3 estados (CLOSED → OPEN → HALF_OPEN)
- **Conceitos:** State pattern, time-based logic, OOP, exception handling
- **Follow-ups prováveis:**
  - Config por serviço (diferentes thresholds por banco) ✅ FEITO
  - Thread safety (adicionar Lock)
  - Métricas/logging (quantas vezes abriu? latência média?)
  - Fallback (em vez de erro, chamar outro banco)

### P2: Currency Converter / Exchange ⭐ (DOMAIN WISE)
- **Arquivo:** `02_currency_converter.py`
- **Cenário:** Implementar serviço de conversão de moedas. Enviar/receber dinheiro.
- **O que constrói:** classes de Account, Currency, Exchange com rates
- **Conceitos:** Domain modeling, edge cases (conta existe? saldo suficiente? moeda suportada?)
- **Follow-ups prováveis:**
  - Adicionar taxas (Wise cobra spread + fee)
  - Exchange rate de moedas sem par direto (BRL→USD→NGN)
  - Rate expiration (rates ficam stale)
  - Refactoring do código pra melhor design

### P3: Simple Cache
- **Arquivo:** `03_simple_cache.py`
- **Cenário:** Implementar um cache in-memory com TTL
- **O que constrói:** get/put com expiração, eviction policy
- **Conceitos:** HashMap, time-based expiration, LRU eviction
- **Follow-ups prováveis:**
  - TTL por chave (diferentes tempos de expiração)
  - Max size + eviction (LRU)
  - Thread safety
  - Cache statistics (hit rate, miss rate)

### P4: Rate Limiter
- **Arquivo:** `04_rate_limiter.py`
- **Cenário:** Limitar requests por cliente/IP. Ex: 100 requests por minuto.
- **O que constrói:** contador com janela de tempo
- **Conceitos:** Sliding window vs fixed window, token bucket, concurrency
- **Follow-ups prováveis:**
  - Sliding window em vez de fixed
  - Diferentes limits por endpoint
  - Distributed rate limiting (Redis)
  - Graceful degradation (429 vs queue)

### P5: Tic-Tac-Toe
- **Arquivo:** `05_tic_tac_toe.py`
- **Cenário:** Implementar jogo da velha com dois jogadores
- **O que constrói:** Board, Player, Game com regras
- **Conceitos:** OOP, state management, win detection
- **Follow-ups prováveis:**
  - Board NxN em vez de 3x3
  - AI opponent (minimax simples)
  - Undo last move
  - Game history

### P6: Intervals (merge/sort)
- **Arquivo:** `06_intervals.py`
- **Cenário:** Duas listas de intervalos de tempo. Merge/sort.
- **O que constrói:** merge overlapping intervals, find intersections
- **Conceitos:** Sorting, two pointers, edge cases
- **Follow-ups prováveis:**
  - Find free slots entre dois calendários
  - Intervalos com prioridade

### P7: Code Refactoring
- **Sem arquivo** — entrevistador dá código ruim, você melhora
- **O que testa:** reconhecer code smells, aplicar SOLID, simplificar
- **Conceitos:** SRP, DIP, extract method, rename, remove duplication
- **Dica:** sempre perguntar "o que esse código deveria fazer?" antes de mexer

## Patterns Importantes pra Wise

| Pattern | O que é | Onde cai |
|---------|---------|----------|
| **State Machine** | Objeto muda comportamento baseado no estado | Circuit Breaker, Tic-Tac-Toe |
| **Strategy** | Trocar algoritmo em runtime | Rate Limiter (fixed vs sliding), Cache (LRU vs LFU) |
| **Observer** | Notificar quando algo muda | Métricas, logging |
| **Template Method** | Esqueleto do algoritmo, subclasses customizam | WebClient com hooks |

## SOLID na Prática (vão avaliar!)

| Princípio | Exemplo nos problemas |
|-----------|----------------------|
| **S** — Single Responsibility | CircuitBreaker separado do WebClient |
| **O** — Open/Closed | Config por serviço sem mudar código do CB |
| **L** — Liskov Substitution | Qualquer Cache (LRU, TTL) implementa mesma interface |
| **I** — Interface Segregation | WebClient não precisa saber dos internals do CB |
| **D** — Dependency Inversion | WebClient recebe CB por construtor (injeção) |

## Dicas Pro Dia

- **Velocidade importa** — candidato rejeitado por lentidão (Oct 2025)
- **Requisitos MUDAM** — não over-engineer na V1, vai ter follow-up
- **Pense em voz alta** — "I'm thinking of using a dict here because..."
- **Peça ajuda** — "What do you think about this approach?"
- **Comece simples** — resolve primeiro, refatora depois
- **Nomes claros** — `record_failure()` não `rf()`
- **Testabilidade** — `_do_request()` separado pra poder mockar
