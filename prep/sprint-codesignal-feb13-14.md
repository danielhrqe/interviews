# Sprint CodeSignal GCA - Feb 13-14

> Deadline: Sab Feb 14 ao meio-dia
> Formato: 4 questoes, 70 min, proctored
> Estrategia: Q1 -> Q2 -> Q4 -> Q3 (Q4 vale mais pontos por tempo)

---

## Formato do CodeSignal GCA

| Questao | Dificuldade | Tempo ideal | Tipo tipico |
|---------|-------------|-------------|-------------|
| Q1 | Easy | 5-10 min | String/Array basico, implementacao direta |
| Q2 | Easy-Medium | 10-15 min | HashMap, arrays, logica com edge cases |
| Q3 | Medium-Hard | 20-25 min | Implementacao pesada, muitas regras (PULAR por ultimo) |
| Q4 | Medium | 15-20 min | Algoritmo/padrao (vale MAIS pontos que Q3!) |

**REGRA DE OURO**: Se travar >5 min em uma questao, pula pra proxima e volta depois.

---

## HOJE - Sexta Feb 13

### Sessao 1: Warm-up + Patterns (90 min) - MANHA

Treinar comigo os 5 padroes que mais caem no GCA:

| # | Padrao | Problema para resolver | Tempo |
|---|--------|----------------------|-------|
| 1 | **HashMap/Counter** | Group Anagrams (LC 49) | 15 min |
| 2 | **String manipulation** | Longest Substring Without Repeating (LC 3) | 15 min |
| 3 | **Array + logica** | Product of Array Except Self (LC 238) | 15 min |
| 4 | **Sorting + intervals** | Merge Intervals (LC 56) | 15 min |
| 5 | **Kadane / subarray** | Maximum Subarray (LC 53) | 15 min |

> Faz cada um no editor online. Se travar, me pede dica. Review da solucao comigo depois.

### Sessao 2: Simulado CodeSignal (70 min) - TARDE

Fazer um **mock timed** comigo simulando o GCA:
- Eu dou 4 problemas no formato CodeSignal
- Voce resolve com timer de 70 min
- Sem consulta (simula proctored)
- Depois: review detalhado de cada solucao

### Sessao 3: Review + Gap-filling (30-45 min) - NOITE

- Revisar erros do simulado
- Praticar os patterns que errou
- Revisar Python essentials:
  - [ ] `collections.Counter` - contar frequencias
  - [ ] `collections.defaultdict` - dicts com valor padrao
  - [ ] `collections.deque` - fila eficiente
  - [ ] `sorted(arr, key=lambda x: x[0])` - sort custom
  - [ ] `"".join()`, `str.split()`, `str.strip()` - strings
  - [ ] List comprehensions `[x for x in arr if cond]`
  - [ ] `enumerate()`, `zip()` - iteracao

---

## AMANHA - Sabado Feb 14

### Sessao 4: Light warm-up (30-45 min) - MANHA CEDO

- 2 problemas Easy para aquecer (nao cansar)
  - [ ] Two Sum (ja sabe, faz em <5 min para confianca)
  - [ ] Valid Parentheses (stack, classico)
- Revisar cheat sheet de Python
- **NAO estudar nada novo** - so reforcar

### PROVA: CodeSignal GCA - ATE MEIO-DIA

Checklist pre-prova:
- [ ] Browser limpo (fechar abas)
- [ ] Internet estavel
- [ ] Webcam/mic funcionando (proctored)
- [ ] Agua do lado
- [ ] Ir ao banheiro antes

Durante a prova:
1. Ler TODAS as 4 questoes primeiro (2 min)
2. Q1: resolver rapido (meta: 8 min)
3. Q2: resolver com cuidado nos edge cases (meta: 15 min)
4. **PULAR Q3** -> ir direto para Q4
5. Q4: resolver (meta: 18 min)
6. Q3: com tempo restante (meta: 20 min)
7. Revisar se sobrar tempo

---

## Padroes Python - Cola Rapida

```python
# HashMap - contar frequencias
from collections import Counter
freq = Counter("aabbc")  # {'a': 2, 'b': 2, 'c': 1}

# defaultdict - agrupar por chave
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.key].append(item)

# Sorting com key
intervals.sort(key=lambda x: x[0])

# Two pointers
left, right = 0, len(arr) - 1
while left < right:
    ...

# Sliding window
left = 0
for right in range(len(arr)):
    window.add(arr[right])
    while condition_violated:
        window.remove(arr[left])
        left += 1

# Kadane (max subarray)
max_sum = cur_sum = nums[0]
for num in nums[1:]:
    cur_sum = max(num, cur_sum + num)
    max_sum = max(max_sum, cur_sum)

# Stack (parentheses)
stack = []
for char in s:
    if char in "({[":
        stack.append(char)
    elif stack and matches(stack[-1], char):
        stack.pop()
    else:
        return False
return len(stack) == 0

# BFS (graph/grid)
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

## Progresso

- [ ] Sessao 1: Warm-up + Patterns (5 problemas)
- [ ] Sessao 2: Simulado mock (4 problemas timed)
- [ ] Sessao 3: Review + gaps
- [ ] Sessao 4: Light warm-up sabado
- [ ] **CodeSignal GCA concluido**
