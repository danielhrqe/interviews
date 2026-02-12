# Coding Interview Roadmap - Cross-Company Analysis

> Atualizado: 10/fev/2026
> Empresas: QuintoAndar (Codility), Wise (HackerRank), Nubank (Take-home + HackerRank), DoorDash (Code Craft)

---

## Panorama das 4 Empresas

| Empresa | Vaga | Plataforma | Formato | Dificuldade | Foco Principal |
|---------|------|-----------|---------|-------------|----------------|
| **QuintoAndar** | Tech Lead MLOps | Codility | Solo, 1h | Easy-Medium | Algoritmos + DS |
| **Wise** | Staff SWE | HackerRank CodePair | Pair programming, 1h | Easy-Medium | Clean code, OOP, prático |
| **Nubank** | Data Infra IC7 | Take-home + HackerRank | Take-home + pair, 1-2h | Easy (live), Medium (take-home) | Clean code, funcional |
| **DoorDash** | EM NV Retail | HackerRank CodePair | Code Craft (raro p/ EM) | Medium-Hard | System design > coding |

---

## Prioridade de Tópicos (por frequência cross-company)

### TIER 1: Aparece em TODAS (estudar primeiro)

| # | Tópico | QA | Wise | Nubank | DD | Tipo de Problema |
|---|--------|----|------|--------|----|-----------------|
| 1 | **HashMap/Dict** | x | x | x | x | Two Sum, grouping, lookups, frequency count |
| 2 | **Arrays/Strings** | x | x | x | x | Two pointers, manipulation, parsing |
| 3 | **Clean Code** | x | x | x | x | Nomes claros, funções pequenas, sem dead code |
| 4 | **Stacks/Queues** | x | x | x | x | Valid parentheses, FIFO processing |
| 5 | **Complexidade (Big O)** | x | x | x | x | Analisar tempo/espaço de cada solução |

### TIER 2: Aparece em 2-3 empresas (estudar depois)

| # | Tópico | QA | Wise | Nubank | DD | Tipo de Problema |
|---|--------|----|------|--------|----|-----------------|
| 6 | **BFS/DFS (grafos/grids)** | x | | | x | Grid traversal, shortest path, multi-source BFS |
| 7 | **Trees** | x | x | | x | BST, traversals, tree comparison |
| 8 | **Sliding Window** | x | | | x | Max subarray, substring problems |
| 9 | **Sorting** | x | x | x | | Interval sorting, custom comparators |
| 10 | **OOP/Design Patterns** | | x | | x | Circuit breaker, rate limiter, classes |
| 11 | **Intervals** | | x | | x | Merge intervals, scheduling |
| 12 | **JSON/stdin-stdout** | | | x | | CLI apps, input/output parsing |

### TIER 3: Específico de 1 empresa (estudar se sobrar tempo)

| # | Tópico | Empresa | Tipo de Problema |
|---|--------|---------|-----------------|
| 13 | **Dynamic Programming** | DoorDash | Job scheduling (LC 1235), longest path |
| 14 | **Heaps/Priority Queue** | DoorDash | K nearest, CPU scheduling |
| 15 | **Functional (map/filter/reduce)** | Nubank | In-memory processing sem DB |
| 16 | **Topological Sort** | DoorDash | Course Schedule, dependencies |
| 17 | **Union-Find** | DoorDash | Connected components, islands |
| 18 | **Graph (weighted)** | Wise | Best exchange rate path |

---

## Problemas Conhecidos por Empresa

### QuintoAndar (Codility)
- Sem problemas específicos reportados
- Codility = geralmente Easy-Medium, foco em correctness + edge cases
- Praticar: arrays, strings, sorting, hash maps, binary search
- **FAZER: Codility demo test**

### Wise
1. Currency Converter (Easy-Medium) - domain problem
2. Circuit Breaker Pattern (Medium) - OOP + estado
3. Rate Limiter (Medium) - concurrency
4. Sorting Two Lists of Intervals (Medium) - intervals
5. Best Exchange Rate (Medium) - graph traversal

### Nubank
1. **Capital Gains Tax Calculator** (Medium) - CLI, JSON, weighted avg, regras fiscais
2. **Job Queue with Precedence** (Medium) - FIFO, priority, skills matching
3. URL Shortener (pair programming)
- **TRAP**: Nunca usar DB! Usar estruturas in-memory + functional patterns

### DoorDash (se cair coding)
1. Nearest DashMart (Medium) - multi-source BFS grid
2. Dasher Max Profit (Hard) - DP interval scheduling
3. Menu Tree (Medium) - recursive tree comparison
4. Nearest Neighbor City (Medium) - HashMap grouping
5. Longest Increasing Path (Hard) - DFS + memoization

---

## Plano de Estudo - 10 dias

### Fase 1: Fundamentos (Dias 1-3) - TODOS PRECISAM

| Dia | Tópico | Exercícios |
|-----|--------|-----------|
| 1 | **HashMap + Arrays** | Two Sum, Valid Anagram, Group Anagrams, Contains Duplicate |
| 2 | **Strings + Two Pointers** | Reverse String, Valid Palindrome, 3Sum, Container With Most Water |
| 3 | **Sorting + Binary Search** | Merge Intervals, Sort Colors, Binary Search, Search Rotated Array |

### Fase 2: Estruturas Core (Dias 4-6)

| Dia | Tópico | Exercícios |
|-----|--------|-----------|
| 4 | **Stacks/Queues + Sliding Window** | Valid Parentheses, Min Stack, Max Sliding Window, Max Vowels Substring |
| 5 | **Trees + BFS/DFS** | Max Depth, Level Order, Validate BST, Invert Tree, Walls and Gates |
| 6 | **Graphs** | Number of Islands, Course Schedule, Clone Graph |

### Fase 3: Problemas Company-Specific (Dias 7-9)

| Dia | Foco | Exercícios |
|-----|------|-----------|
| 7 | **Nubank prep** | Capital Gains Calculator (take-home), JSON parsing, functional patterns |
| 8 | **Wise prep** | Circuit Breaker impl, Rate Limiter, Interval problems, OOP |
| 9 | **DoorDash prep** | Nearest DashMart (BFS grid), Dasher Max Profit (DP), Menu Tree |

### Fase 4: Mock + Review (Dia 10)

| Dia | Atividade |
|-----|-----------|
| 10 | Codility demo test + revisão de gaps + mock timed |

---

## Checklist de Habilidades (para diagnóstico)

### Estruturas de Dados
- [ ] Array/List: acesso O(1), append O(1), insert O(n)
- [ ] HashMap/Dict: get/set O(1), quando usar, colisões
- [ ] Stack (LIFO): push/pop, valid parentheses
- [ ] Queue (FIFO): enqueue/dequeue, BFS
- [ ] Heap: min/max, priority queue, O(log n) insert
- [ ] Tree: BST, DFS (in/pre/post), BFS (level order)
- [ ] Graph: adjacency list, BFS, DFS, topological sort
- [ ] Linked List: fast/slow pointers, reversal

### Padrões de Algoritmo
- [ ] Two Pointers: sorted array, palindrome
- [ ] Sliding Window: fixed/variable size, max subarray
- [ ] Binary Search: sorted array, search space reduction
- [ ] BFS: shortest path, level order, multi-source
- [ ] DFS: graph/tree traversal, backtracking
- [ ] Dynamic Programming: memoization, tabulation
- [ ] Greedy: interval scheduling, best local choice
- [ ] Sorting: merge sort, quicksort, custom comparators

### Python Essentials
- [ ] List comprehensions
- [ ] Dict/set operations
- [ ] Collections: Counter, defaultdict, deque
- [ ] Sorting com key functions
- [ ] String manipulation
- [ ] map/filter/reduce (Nubank)
- [ ] Classes e OOP (Wise/DoorDash)

### Clean Code
- [ ] Nomes descritivos
- [ ] Funções pequenas com responsabilidade única
- [ ] Sem dead code
- [ ] Edge cases tratados
- [ ] Complexidade analisada

---

## LeetCode Problems - Top 30 Cross-Company

| # | Problema | LC# | Padrão | Dificuldade | Empresas |
|---|----------|-----|--------|-------------|----------|
| 1 | Two Sum | 1 | HashMap | Easy | ALL |
| 2 | Valid Parentheses | 20 | Stack | Easy | ALL |
| 3 | Merge Intervals | 56 | Sort + Intervals | Medium | Wise, DD |
| 4 | Group Anagrams | 49 | HashMap | Medium | QA, Nubank |
| 5 | Contains Duplicate | 217 | HashSet | Easy | ALL |
| 6 | Best Time Buy/Sell Stock | 121 | Sliding Window | Easy | ALL |
| 7 | Valid Palindrome | 125 | Two Pointers | Easy | ALL |
| 8 | Number of Islands | 200 | BFS/DFS Grid | Medium | QA, DD |
| 9 | Binary Tree Level Order | 102 | BFS Tree | Medium | QA, DD |
| 10 | Maximum Depth Binary Tree | 104 | DFS Tree | Easy | ALL |
| 11 | Course Schedule | 207 | Topological Sort | Medium | DD |
| 12 | 01 Matrix | 542 | Multi-source BFS | Medium | DD |
| 13 | Walls and Gates | 286 | Multi-source BFS | Medium | DD |
| 14 | Max Profit Job Scheduling | 1235 | DP + BinSearch | Hard | DD |
| 15 | 3Sum | 15 | Two Pointers | Medium | QA, Wise |
| 16 | Container With Most Water | 11 | Two Pointers | Medium | QA |
| 17 | Search in Rotated Array | 33 | Binary Search | Medium | QA |
| 18 | Min Stack | 155 | Stack | Medium | ALL |
| 19 | Longest Substring No Repeat | 3 | Sliding Window | Medium | QA, Wise |
| 20 | Validate BST | 98 | DFS Tree | Medium | QA, DD |
| 21 | Invert Binary Tree | 226 | DFS Tree | Easy | ALL |
| 22 | Clone Graph | 133 | BFS/DFS Graph | Medium | DD |
| 23 | Sort Colors | 75 | Two Pointers | Medium | QA |
| 24 | Climbing Stairs | 70 | DP | Easy | QA |
| 25 | Product of Array Except Self | 238 | Array | Medium | QA, Nubank |
| 26 | Longest Increasing Path Matrix | 329 | DFS + Memo | Hard | DD |
| 27 | Design Browser History | 1472 | Stack/DLL | Medium | DD |
| 28 | Valid Sudoku | 36 | HashSet | Medium | DD |
| 29 | Maximum Subarray | 53 | Kadane/DP | Medium | ALL |
| 30 | Binary Search | 704 | Binary Search | Easy | ALL |
