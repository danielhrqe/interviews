# Cheatsheet - Algoritmos & Estruturas

## Binary Search
- Busca em lista **ordenada**, descarta metade a cada passo
- O(log n)
- Template: `left, right` → `while left <= right` → `mid` → compara → move `left = mid+1` ou `right = mid-1`

## BFS (Breadth-First Search) — Busca em Largura
- Explora **vizinhos primeiro**, camada por camada (como onda na água)
- Usa **fila (deque)**: append + popleft (FIFO)
- Em grid: percorre célula por célula, achou alvo → BFS nos 4 vizinhos (cima, baixo, esquerda, direita)
- Marca visitado pra não repetir
- Uso clássico: contar ilhas, menor caminho em grid

## HashMap (dict)
- Chave → valor, busca O(1)
- Padrão Two Sum: guarda complemento no dict enquanto percorre

## Stack (pilha)
- LIFO: último a entrar, primeiro a sair
- Python: lista com `append()` e `pop()`
- Uso: parênteses válidos, desfazer operações

## Queue (fila)
- FIFO: primeiro a entrar, primeiro a sair
- Python: `deque` com `append()` e `popleft()`
- Uso: BFS, processar em ordem

## Counter
- Conta ocorrências automaticamente: `Counter([1,2,2,3])` → `{2:2, 3:1, 1:1}`
- `.most_common(n)` → os n mais frequentes
- Funciona com strings: `Counter("banana")` → `{'a':3, 'n':2, 'b':1}`

## defaultdict
- Dict que nunca dá KeyError, cria valor padrão sozinho
- `defaultdict(list)` → chave nova vira `[]`
- `defaultdict(int)` → chave nova vira `0`
- `defaultdict(set)` → chave nova vira `set()`
- Uso: agrupar dados por chave sem checar `if key in dict`

## Sliding Window
- Janela deslizante sobre array/string
- Mantém soma/contagem da janela, ajusta incrementalmente (adiciona novo, remove antigo)
- Uso: maior substring sem repetição, soma máxima de subarray de tamanho k

## Two Pointers
- Dois ponteiros que se movem pela lista (geralmente um do início, outro do fim)
- Uso: palíndromo, remover duplicatas in-place, container with most water

## Sorting
- Python: `sorted(lista)` retorna nova lista, `lista.sort()` ordena in-place
- Ordenar por critério: `sorted(lista, key=lambda x: x[1])`
- O(n log n)