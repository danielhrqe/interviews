# Cracking the Coding Interview - Base de Conhecimento Completa

> Referencia: "Cracking the Coding Interview" (6a ed.) por Gayle Laakmann McDowell
> Compilado para: Engenheiro experiente (10 anos) em transicao de gestao para IC/Staff

---

## Indice

1. [O Processo de Entrevista](#1-o-processo-de-entrevista)
2. [Por Tras dos Bastidores](#2-por-tras-dos-bastidores)
3. [Situacoes Especiais](#3-situacoes-especiais)
4. [Antes da Entrevista](#4-antes-da-entrevista)
5. [Perguntas Comportamentais](#5-perguntas-comportamentais)
6. [Big O - Complexidade](#6-big-o---complexidade)
7. [Abordagem para Resolver Problemas](#7-abordagem-para-resolver-problemas)
8. [Arrays e Strings](#8-arrays-e-strings)
9. [Linked Lists](#9-linked-lists)
10. [Stacks e Queues](#10-stacks-e-queues)
11. [Trees e Graphs](#11-trees-e-graphs)
12. [Bit Manipulation](#12-bit-manipulation)
13. [Matematica e Puzzles Logicos](#13-matematica-e-puzzles-logicos)
14. [Design Orientado a Objetos](#14-design-orientado-a-objetos)
15. [Recursao e Programacao Dinamica](#15-recursao-e-programacao-dinamica)
16. [System Design e Escalabilidade](#16-system-design-e-escalabilidade)
17. [Sorting e Searching](#17-sorting-e-searching)
18. [Testing](#18-testing)
19. [Databases e SQL](#19-databases-e-sql)
20. [Threads e Locks](#20-threads-e-locks)
21. [Padroes Comuns de Entrevista](#21-padroes-comuns-de-entrevista)
22. [Dicas e Estrategias](#22-dicas-e-estrategias)

---

## 1. O Processo de Entrevista

### Como funciona uma entrevista tecnica

Uma entrevista tecnica tipica dura **45 minutos a 1 hora** e segue este formato:

1. **Conversa inicial** (5 min) - O entrevistador se apresenta, pergunta sobre voce
2. **Problema tecnico** (30-40 min) - Resolver 1-2 problemas de codigo
3. **Perguntas do candidato** (5 min) - Voce pergunta sobre a empresa/time

### O que os entrevistadores avaliam

Os entrevistadores avaliam voce em **quatro dimensoes principais**:

| Dimensao | O que observam |
|----------|---------------|
| **Habilidades Analiticas** | Como voce estruturou o problema? Considerou trade-offs? |
| **Habilidades de Codigo** | Traduziu o algoritmo em codigo razoavel? Considerou edge cases? |
| **Conhecimento Tecnico** | Tem base solida em CS fundamentals? |
| **Experiencia / Cultura** | Se encaixa na cultura? Consegue comunicar bem? |

### Mitos importantes

- **"Preciso acertar tudo"**: FALSO. Ninguem espera perfeicao. O processo importa mais que o resultado.
- **"Respostas rapidas sao melhores"**: FALSO. O entrevistador quer ver seu raciocinio, nao velocidade.
- **"Se errei, estou fora"**: FALSO. Muitos candidatos contratados erraram algo. O que importa e como voce reagiu.
- **"Problemas de entrevista sao inuteis"**: Discutivel, mas sao a realidade. Aceite e prepare-se.

### Como candidatos sao avaliados

- Cada entrevistador da uma nota (geralmente 1-4 ou Hire/No Hire)
- As notas sao discutidas em **comite de contratacao** (hiring committee)
- Um entrevistador sozinho geralmente NAO tem poder de veto
- Em empresas como Google, o comite e separado dos entrevistadores
- **Falsos negativos sao aceitaveis** para as empresas (rejeitar bom candidato e ok, contratar mau candidato nao)

---

## 2. Por Tras dos Bastidores

### Como cada grande empresa contrata

#### Google
- **Processo**: Phone screen -> 4-5 entrevistas on-site -> Hiring Committee -> Aprovacao de lideranca
- **Diferencial**: O hiring committee e separado dos entrevistadores. Eles leem feedback escrito.
- **Dica**: Escreva codigo limpo. O comite vai ler o que o entrevistador anotou.
- Entrevistadores avaliam mas **nao decidem**. A decisao e do comite.

#### Amazon
- **Processo**: Phone screen -> 4-5 entrevistas on-site com o "Bar Raiser"
- **Bar Raiser**: Um entrevistador especial treinado de outro time que tem poder de veto
- **Foco**: Leadership Principles sao centrais. Prepare historias usando cada um.
- **Dica**: Conecte cada resposta comportamental a um Leadership Principle.

#### Meta (Facebook)
- **Processo**: Phone screen -> On-site com 3 papeis: "Ninja" (coding), "Jedi" (behavioral), "Pirate" (system design)
- **Diferencial**: Bootcamp de 6 semanas apos contratacao. Voce escolhe o time depois.
- **Dica**: System design e fortemente avaliado para candidatos senior.

#### Microsoft
- **Processo**: Phone screen -> 4-5 entrevistas on-site -> "As Appropriate" interview com hiring manager
- **Diferencial**: O ultimo entrevistador ("As Appropriate") e quem toma a decisao final.
- **Dica**: Se voce chegar no "As Appropriate", esta perto. De o seu melhor.

#### Apple
- **Processo**: Phone screen -> 6-8 entrevistas on-site (sim, muitas)
- **Diferencial**: Entrevistas 2-on-1 sao comuns. Menos burocracia que Google.
- **Foco**: Paixao pelo produto e pela empresa importa muito.

### Takeaway para candidatos experientes

Para posicoes de Staff/Lead, espere:
- Mais enfase em **system design**
- Perguntas comportamentais mais profundas sobre **lideranca e impacto**
- Codigo ainda e avaliado, mas com expectativa de **maturidade** (tratar edge cases, pensar em producao)

---

## 3. Situacoes Especiais

### Candidatos Experientes (10+ anos)

Este e o seu caso. Pontos importantes:

- **O que muda**: Esperam respostas mais profundas e maduras. "Qual foi o bug mais dificil?" precisa ser uma historia impressionante.
- **System Design pesa mais**: Para niveis senior/staff, system design pode ser 40-50% da avaliacao.
- **Codigo ainda importa**: Nao pense que pode pular coding por ser senior. Voce ainda precisa codar.
- **Suas experiencias sao um ativo**: Use exemplos reais para ilustrar trade-offs.

### Gestores voltando para IC (Individual Contributor)

> **Diretamente relevante para voce**

- **Desafio principal**: Provar que ainda consegue codar, nao apenas gerenciar
- **Expectativa dos entrevistadores**: Acham que voce pode ter "enferrujado" em codigo
- **Estrategia**: Pratique mais coding do que candidatos que nunca sairam de IC
- **Vantagem competitiva**: Experiencia com system design, comunicacao, lideranca tecnica
- **Como usar sua experiencia**: Em system design, traga exemplos reais. Em behavioral, demonstre que pode voltar ao "hands-on"

### Dev Leads e Managers (entrevistando para gestao)

- Demonstre que consegue comunicar em **multiplos niveis** (tecnico com eng, estrategico com direcao)
- Conte historias sobre **resolver conflitos**, **priorizar**, **desenvolver pessoas**
- Prepare exemplos de **decisoes tecnicas dificeis** que voce tomou ou guiou

### Startups vs Big Tech

| Aspecto | Startup | Big Tech |
|---------|---------|----------|
| Processo | Menos estruturado | Muito estruturado |
| Entrevistadores | Founders, CTO | Engenheiros treinados |
| Foco | "Voce resolve nosso problema?" | "Voce e bom no geral?" |
| Negociacao | Mais equity, salario flexivel | Bandas salariais, equity padrao |

---

## 4. Antes da Entrevista

### Curriculo / Resume

**Regras de ouro para engenheiros experientes:**

1. **Uma pagina** (sim, mesmo com 10 anos - selecione o melhor)
2. **Resultados, nao responsabilidades**: "Reduzi latencia em 40%" > "Responsavel pelo sistema de cache"
3. **Numeros sempre que possivel**: "Lideranca de time de 8 engenheiros", "Sistema processando 50M requests/dia"
4. **Projetos relevantes**: Destaque 2-3 projetos mais impactantes
5. **Linguagens e tecnologias**: Liste as que voce realmente domina
6. **Sem erros**: Qualquer erro pode desqualificar (falta de atencao a detalhe)

**Template de bullet point:**
```
"[Verbo de acao] [o que fez] usando [tecnologia], resultando em [impacto mensuravel]"

Exemplo:
"Arquitetei pipeline de dados usando Spark e Airflow, reduzindo tempo de processamento de 8h para 45min"
```

### Linha do tempo de preparacao

| Periodo | Atividade |
|---------|-----------|
| **4+ semanas antes** | Estudar estruturas de dados e algoritmos |
| **2-3 semanas antes** | Praticar problemas diariamente (LeetCode, HackerRank) |
| **1 semana antes** | Mock interviews, revisar system design |
| **Dia anterior** | Descansar, revisar anotacoes rapidas |

---

## 5. Perguntas Comportamentais

### O Grid de Preparacao (Story Grid)

Crie uma **matriz de historias** antes da entrevista:

|                     | Projeto A | Projeto B | Projeto C |
|---------------------|-----------|-----------|-----------|
| **Desafio Tecnico** | historia  | historia  | historia  |
| **Conflito no time**| historia  | historia  | historia  |
| **Fracasso/Erro**   | historia  | historia  | historia  |
| **Lideranca**       | historia  | historia  | historia  |
| **Decisao dificil** | historia  | historia  | historia  |

**Como preencher**: Para cada celula, escreva 2-3 palavras-chave que te lembrem da historia.

### Metodo SAR/STAR

Use esta estrutura para TODA resposta comportamental:

```
S - Situacao (20%): Contextualize brevemente (1-2 frases)
T - Tarefa (10%):   O que voce precisava resolver
A - Acao (60%):     O que VOCE especificamente fez (detalhe aqui!)
R - Resultado (10%): O impacto mensuravel
```

**Exemplo ruim:**
> "Tinhamos um problema de performance. O time investigou e resolveu."

**Exemplo bom:**
> "**Situacao**: Nosso pipeline de ML tinha latencia de 8h, bloqueando o time de data science.
> **Tarefa**: Eu precisava reduzir para menos de 1h sem aumentar custos.
> **Acao**: Analisei o bottleneck e identifiquei que 70% do tempo era I/O em disco. Reprojetei o pipeline usando processamento em memoria com Spark, implementei particionamento por data, e criei cache para features intermediarias. Liderei a migracao com 3 engenheiros em 4 sprints.
> **Resultado**: Latencia caiu para 45min, custos reduziram 20%, e o time de DS ganhou ciclos de iteracao 10x mais rapidos."

### Perguntas comportamentais mais comuns

1. **"Conte sobre um desafio tecnico que voce superou"**
2. **"Descreva um conflito com um colega e como resolveu"**
3. **"Fale sobre um projeto que fracassou"**
4. **"Qual sua maior conquista tecnica?"**
5. **"Como voce lida com prioridades conflitantes?"**
6. **"Por que voce quer sair da gestao e voltar para IC?"** (prepare esta com cuidado!)
7. **"Como voce liderou uma decisao tecnica controversa?"**

### Dica para ex-gestores

Quando perguntarem "por que voltar para IC":
- Seja **honesto e positivo**: "Sinto falta de resolver problemas tecnicos complexos"
- **Nao fale mal de gestao**: "Valorizei a experiencia, mas minha paixao e construir"
- **Mostre que e intencional**: "Quero usar minha experiencia de gestao com um foco tecnico mais profundo"

---

## 6. Big O - Complexidade

### O que e Big O

Big O descreve como o **tempo de execucao** ou **uso de memoria** de um algoritmo cresce em relacao ao tamanho da entrada (n). Nao e sobre o tempo exato, mas sobre a **taxa de crescimento**.

### Complexidades mais comuns (da mais rapida para mais lenta)

| Big O | Nome | Exemplo | Tempo para n=1M |
|-------|------|---------|-----------------|
| O(1) | Constante | Acesso a indice de array, lookup em hash | instantaneo |
| O(log n) | Logaritmica | Binary search | ~20 operacoes |
| O(n) | Linear | Loop simples, busca linear | 1M operacoes |
| O(n log n) | Log-linear | Merge sort, sort otimizado | ~20M operacoes |
| O(n^2) | Quadratica | Loop aninhado, bubble sort | 1 trilhao ops |
| O(2^n) | Exponencial | Subsets, recursao sem memo | impossivel |
| O(n!) | Fatorial | Permutacoes | impossivel |

### Como analisar complexidade

**Regras praticas:**

```python
# O(1) - Constante
x = arr[5]                    # Acesso direto

# O(n) - Linear
for item in arr:              # Um loop
    print(item)

# O(n^2) - Quadratica
for i in arr:                 # Loop aninhado
    for j in arr:
        print(i, j)

# O(log n) - Logaritmica
while n > 0:                  # Dividindo pela metade
    n = n // 2

# O(n log n) - Log-linear
arr.sort()                    # Sorting otimizado
```

**Regras de simplificacao:**
1. **Descarte constantes**: O(2n) -> O(n)
2. **Descarte termos menores**: O(n^2 + n) -> O(n^2)
3. **Loops sequenciais somam**: O(n) + O(m) = O(n + m)
4. **Loops aninhados multiplicam**: O(n) * O(m) = O(n * m)

### Complexidade de espaco (Space Complexity)

Nao esqueca do espaco! Muitas otimizacoes trocam espaco por tempo.

```python
# O(1) espaco - modificando in-place
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# O(n) espaco - criando nova estrutura
def reverse_copy(arr):
    return arr[::-1]  # Cria copia

# O(n) espaco - call stack de recursao
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # n frames na stack
```

### Analise Amortizada

Algumas operacoes sao O(1) **amortizado** - ou seja, na maioria das vezes sao O(1), mas ocasionalmente sao O(n).

**Exemplo classico: `list.append()` em Python**

```python
# Python list usa array dinamico
# Quando o array esta cheio, aloca 2x o tamanho e copia tudo
# Append: O(1) amortizado, O(n) no pior caso (quando precisa realocar)
arr = []
for i in range(1000000):
    arr.append(i)  # Maioria e O(1), algumas sao O(n)
    # Mas no total: n operacoes custam O(n) -> media O(1) cada
```

### Dicas para entrevista

1. **Sempre declare a complexidade** apos apresentar sua solucao
2. **Mencione trade-offs**: "Posso fazer O(n) tempo com O(n) espaco, ou O(n^2) tempo com O(1) espaco"
3. **Log base nao importa**: O(log2 n) = O(log10 n) em Big O (diferem por constante)
4. **Recursao**: Lembre que cada chamada recursiva usa espaco na call stack

---

## 7. Abordagem para Resolver Problemas

### Os 7 Passos do CTCI

Este e o framework mais importante do livro. **Memorize e pratique.**

#### Passo 1: OUVIR (Listen)

- Preste atencao a **cada detalhe** do enunciado
- Detalhes sao pistas: "array **ordenado**" -> two pointers ou binary search
- Pergunte para clarificar: tamanho da entrada, tipos de dados, restricoes

**Checklist de perguntas:**
- Qual o tamanho da entrada?
- Os dados estao ordenados?
- Pode haver duplicados?
- Pode haver valores negativos?
- Qual o output esperado?

#### Passo 2: CRIAR EXEMPLO (Draw Example)

- Crie um exemplo **especifico** (com numeros reais)
- **Suficientemente grande** (nao use arrays de 2-3 elementos)
- **Nao use caso especial** (nao use array ja ordenado se nao for garantido)

**Exemplo ruim**: `[1, 2, 3]`
**Exemplo bom**: `[4, 1, 7, 2, 9, 3, 8]`

#### Passo 3: FORCA BRUTA (Brute Force)

- Encontre a solucao mais simples e obvia, **mesmo que seja lenta**
- Declare a complexidade
- Diga ao entrevistador: "Primeiro, vou comecar com a solucao brute force"

```python
# Exemplo: encontrar dois numeros que somam target
# Brute force: O(n^2)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

#### Passo 4: OTIMIZAR (Optimize)

Use a tecnica **BUD** para encontrar otimizacoes:

- **B - Bottlenecks (Gargalos)**: Qual parte e mais lenta? Posso melhorar?
- **U - Unnecessary work (Trabalho desnecessario)**: Estou fazendo algo que nao preciso?
- **D - Duplicated work (Trabalho duplicado)**: Estou recalculando algo? Posso cachear?

**Outras tecnicas de otimizacao:**
- **Hash map**: Troca espaco por tempo (O(n^2) -> O(n))
- **Sorting**: Ordenar primeiro pode simplificar o problema
- **Two pointers**: Para arrays ordenados
- **Sliding window**: Para subarrays contiguos
- **Space/time trade-off**: Usar mais memoria para reduzir tempo

```python
# Otimizado: O(n) com hash map
def two_sum_optimized(nums, target):
    seen = {}  # valor -> indice
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

#### Passo 5: PERCORRER A SOLUCAO (Walk Through)

- Antes de codar, percorra a solucao **passo a passo** com seu exemplo
- Verifique que cada detalhe funciona
- Pense em edge cases
- Confirme a nova complexidade

#### Passo 6: ESCREVER CODIGO LIMPO (Code)

- **Nomes descritivos**: `left`, `right` ao inves de `i`, `j` (quando fizer sentido)
- **Modularize**: Extraia funcoes auxiliares se o codigo ficar complexo
- **Comece do topo**: Escreva a funcao principal primeiro, auxiliares depois
- **Estilo profissional**: Voce e senior, seu codigo deve refletir isso

#### Passo 7: TESTAR (Test)

- **Nao rode o codigo mentalmente line by line** - isso e lento e propenso a erros
- **Analise conceitual primeiro**: O algoritmo faz sentido?
- **Teste com seu exemplo**
- **Teste edge cases**: array vazio, um elemento, todos iguais, negativos
- **Hot spots**: null checks, limites de loops, off-by-one errors

---

## 8. Arrays e Strings

### Conceitos fundamentais

**Arrays em Python** sao implementados como `list` - arrays dinamicos que crescem automaticamente.

| Operacao | Complexidade | Notas |
|----------|-------------|-------|
| Acesso por indice | O(1) | `arr[i]` |
| Append | O(1) amortizado | `arr.append(x)` |
| Insert no inicio | O(n) | `arr.insert(0, x)` - desloca tudo |
| Delete por indice | O(n) | `arr.pop(i)` - desloca tudo |
| Search (nao ordenado) | O(n) | `x in arr` |
| Search (ordenado) | O(log n) | Binary search |
| Sort | O(n log n) | `arr.sort()` - Timsort |
| Slice | O(k) | `arr[i:j]` onde k = j - i |

**Strings em Python** sao **imutaveis**. Cada concatenacao cria nova string.

```python
# RUIM - O(n^2) pois cada += cria nova string
result = ""
for char in text:
    result += char

# BOM - O(n) usando lista e join
parts = []
for char in text:
    parts.append(char)
result = "".join(parts)

# MELHOR - list comprehension
result = "".join([char for char in text])
```

### Tecnicas essenciais

#### Hash Tables (dict em Python)

O(1) para insert, delete, lookup. Use para contagem, mapeamento, deduplicacao.

```python
# Contagem de frequencia
from collections import Counter
freq = Counter("abracadabra")  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Checar anagrama
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```

#### Two Pointers

Use quando o array esta **ordenado** ou quando precisa comparar elementos.

```python
# Remover duplicados de array ordenado in-place
def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

# Verificar palindromo
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

#### Sliding Window

Use para problemas de **subarrays/substrings** contiguos.

```python
# Maior soma de subarray de tamanho k
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Desliza: adiciona novo, remove antigo
        max_sum = max(max_sum, window_sum)

    return max_sum

# Menor substring contendo todos os caracteres
def min_window_substring(s, t):
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (0, float('inf'))  # (start, end)

    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        while missing == 0:  # Temos todos os chars
            if right - left < best[1] - best[0]:
                best = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1

    return s[best[0]:best[1] + 1] if best[1] != float('inf') else ""
```

### Problemas classicos

1. **Is Unique**: Verificar se string tem todos caracteres unicos -> set() ou bit manipulation
2. **Check Permutation**: Verificar se uma string e permutacao de outra -> Counter
3. **URLify**: Substituir espacos por '%20' -> two pointers de tras para frente
4. **Palindrome Permutation**: Checar se alguma permutacao e palindromo -> no maximo 1 char com freq impar
5. **String Compression**: "aabcccccaaa" -> "a2b1c5a3" -> StringBuilder pattern
6. **Two Sum**: Encontrar par que soma target -> hash map

### Erros comuns

- Esquecer que strings sao **imutaveis** em Python (concatenacao e O(n))
- Off-by-one em indices de sliding window
- Nao considerar array vazio ou com um elemento
- Nao considerar duplicados
- Esquecer de converter entre maiusculas/minusculas

---

## 9. Linked Lists

### Conceitos fundamentais

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

| Operacao | Array | Linked List |
|----------|-------|-------------|
| Acesso por indice | O(1) | O(n) |
| Insert/Delete no inicio | O(n) | O(1) |
| Insert/Delete no fim | O(1) amortizado | O(n)* |
| Search | O(n) | O(n) |
| Insert/Delete no meio (dado ponteiro) | O(n) | O(1) |

*O(1) se tiver ponteiro para o ultimo no

### Tecnicas essenciais

#### Dummy Node (Sentinela)

Simplifica operacoes no inicio da lista.

```python
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
```

#### Runner Technique (Dois Ponteiros)

Usar dois ponteiros com velocidades diferentes.

```python
# Encontrar o meio da lista
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next       # 1 passo
        fast = fast.next.next  # 2 passos
    return slow  # Quando fast chega ao fim, slow esta no meio

# Detectar ciclo (Floyd's Algorithm)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Encontrar inicio do ciclo
def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Encontrou ciclo - agora achar o inicio
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

#### Reverter uma Linked List

Problema **extremamente comum**. Memorize.

```python
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Salva o proximo
        current.next = prev       # Reverte o ponteiro
        prev = current            # Avanca prev
        current = next_node       # Avanca current
    return prev  # Novo head
```

### Problemas classicos

1. **Remove Duplicates**: Hash set para rastrear vistos, ou dois ponteiros se ordenada
2. **Kth to Last**: Dois ponteiros com distancia k entre eles
3. **Delete Middle Node**: Copiar valor do proximo e deletar proximo (sem acesso ao head)
4. **Partition**: Criar duas listas (menores e maiores), concatenar
5. **Sum Lists**: Somar digito a digito com carry
6. **Palindrome**: Reverter metade e comparar, ou usar stack
7. **Intersection**: Calcular tamanhos, alinhar, percorrer juntos

### Erros comuns

- Perder referencia ao `next` antes de redirecionar ponteiros
- Esquecer do caso de lista vazia (`head is None`)
- Nao usar dummy node e complicar a logica de edge cases
- Nao tratar lista com um unico elemento
- Criar ciclo acidentalmente

---

## 10. Stacks e Queues

### Stack (LIFO - Last In, First Out)

```python
# Stack com list (recomendado em Python)
stack = []
stack.append(1)     # push - O(1)
stack.append(2)
stack.append(3)
top = stack[-1]     # peek - O(1) -> 3
val = stack.pop()   # pop - O(1) -> 3
is_empty = len(stack) == 0
```

### Queue (FIFO - First In, First Out)

```python
from collections import deque

# Queue com deque (NUNCA use list para queue!)
queue = deque()
queue.append(1)      # enqueue - O(1)
queue.append(2)
queue.append(3)
front = queue[0]     # peek - O(1) -> 1
val = queue.popleft() # dequeue - O(1) -> 1

# POR QUE NAO usar list:
# list.pop(0) e O(n) - desloca todos os elementos!
# deque.popleft() e O(1) - otimizado para isso
```

### Quando usar cada um

| Use Stack quando... | Use Queue quando... |
|--------------------|---------------------|
| Precisa processar na ordem reversa | Precisa processar na ordem de chegada |
| Desfazer operacoes (undo) | BFS em grafos/arvores |
| Validar parenteses | Buffer de processamento |
| Avaliar expressoes | Scheduler de tarefas |
| DFS iterativo | Processamento em niveis |

### Problemas classicos

#### Valid Parentheses (Stack)

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

# Testes
assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([)]") == False
assert is_valid("{[]}") == True
```

#### Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Stack auxiliar para rastrear minimos

    def push(self, val):
        self.stack.append(val)
        # Empilha se for menor ou igual ao minimo atual
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def get_min(self):
        return self.min_stack[-1]  # O(1)!
```

#### Queue usando duas Stacks

```python
class QueueViaStacks:
    def __init__(self):
        self.stack_in = []   # Para enqueue
        self.stack_out = []  # Para dequeue

    def enqueue(self, val):
        self.stack_in.append(val)

    def dequeue(self):
        if not self.stack_out:
            # Transfere tudo de in para out (inverte a ordem)
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
    # Amortizado O(1) por operacao!
```

#### Monotonic Stack

Util para encontrar "proximo elemento maior/menor".

```python
# Proximo elemento maior para cada posicao
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # Guarda indices

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result

# next_greater_element([2, 1, 2, 4, 3]) -> [4, 2, 4, -1, -1]
```

---

## 11. Trees e Graphs

### Arvores Binarias - Conceitos

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Terminologia:**
- **Root**: No raiz (topo)
- **Leaf**: No folha (sem filhos)
- **Height**: Distancia da raiz ate a folha mais distante
- **Depth**: Distancia de um no ate a raiz
- **Balanced**: Diferenca de altura entre sub-arvores <= 1

### Tipos de arvores

| Tipo | Definicao | Uso |
|------|-----------|-----|
| **Binary Tree** | Cada no tem no maximo 2 filhos | Base para BST, heaps |
| **BST** | Esquerda < no < Direita | Busca ordenada O(log n) |
| **Balanced BST** | BST com altura O(log n) | AVL, Red-Black trees |
| **Heap** | Pai >= filhos (max) ou Pai <= filhos (min) | Priority queue |
| **Trie** | Arvore de prefixos, cada aresta e um caractere | Autocomplete, dicionarios |
| **N-ary Tree** | Cada no pode ter N filhos | Filesystem, org charts |

### Traversals (Percursos) - FUNDAMENTAL

```python
# DFS - Tres ordens (MEMORIZE!)
def inorder(root):      # Esquerda -> No -> Direita (BST: ordem crescente!)
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):     # No -> Esquerda -> Direita (copia da arvore)
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):    # Esquerda -> Direita -> No (deletar arvore)
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# BFS - Por niveis (usa queue!)
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result
```

### Binary Search Tree (BST)

```python
# Busca em BST - O(log n) em arvore balanceada
def search_bst(root, target):
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# Insercao em BST
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# Validar BST (armadilha classica!)
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))
```

### Heap / Priority Queue

```python
import heapq

# Min heap (padrao em Python)
heap = []
heapq.heappush(heap, 5)    # O(log n)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
min_val = heap[0]           # O(1) - peek
min_val = heapq.heappop(heap)  # O(log n) - extrai minimo

# Max heap (truque: negue os valores)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap)  # 5

# K maiores elementos - O(n log k)
def k_largest(nums, k):
    return heapq.nlargest(k, nums)

# Mediana corrente usando dois heaps
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (metade menor, valores negados)
        self.large = []  # min heap (metade maior)

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        # Garante que max(small) <= min(large)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balanceia tamanhos
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### Trie (Arvore de Prefixos)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):    # O(m) onde m = len(word)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):    # O(m)
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):  # O(m)
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

### Grafos

**Representacoes:**

```python
# Lista de adjacencia (mais comum em entrevistas)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Tambem pode usar defaultdict
from collections import defaultdict
graph = defaultdict(list)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D')]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Se nao-direcionado
```

#### BFS em Grafo

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Caminho mais curto (BFS garante menor numero de arestas)
def shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # Sem caminho
```

#### DFS em Grafo

```python
# Recursivo
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Iterativo (usando stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
```

#### Topological Sort (DAG)

```python
from collections import deque, defaultdict

def topological_sort(num_nodes, edges):
    """Kahn's Algorithm - BFS-based topological sort"""
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Comeca com nos sem dependencias
    queue = deque([n for n in range(num_nodes) if in_degree[n] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Se nao visitou todos, tem ciclo
    return order if len(order) == num_nodes else []
```

#### Union-Find (Disjoint Set)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Numero de componentes

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Ja conectados
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Problemas classicos

**Arvores:**
1. Altura da arvore
2. Verificar se e balanceada
3. Validar BST
4. Lowest Common Ancestor (LCA)
5. Serializar/deserializar arvore
6. Caminho com maior soma

**Grafos:**
1. Detectar ciclo (DFS com cores ou Union-Find)
2. Numero de ilhas (BFS/DFS em grid)
3. Clone de grafo
4. Topological sort (course schedule)
5. Caminho mais curto (BFS, Dijkstra)
6. Numero de componentes conectados

---

## 12. Bit Manipulation

### Operacoes basicas

```python
# AND (&) - ambos 1
5 & 3   # 101 & 011 = 001 = 1

# OR (|) - pelo menos um 1
5 | 3   # 101 | 011 = 111 = 7

# XOR (^) - exatamente um 1
5 ^ 3   # 101 ^ 011 = 110 = 6

# NOT (~) - inverte todos os bits
~5      # ~0101 = ...1010 = -6 (complemento de 2)

# Left Shift (<<) - multiplica por 2^n
5 << 1  # 101 << 1 = 1010 = 10
1 << 3  # 1 << 3 = 1000 = 8

# Right Shift (>>) - divide por 2^n
8 >> 1  # 1000 >> 1 = 100 = 4
```

### Truques essenciais

```python
# Verificar se bit na posicao i esta setado
def get_bit(num, i):
    return (num >> i) & 1

# Setar bit na posicao i
def set_bit(num, i):
    return num | (1 << i)

# Limpar bit na posicao i
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle bit na posicao i
def toggle_bit(num, i):
    return num ^ (1 << i)

# Verificar se e potencia de 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
    # Truque: potencia de 2 tem apenas 1 bit setado
    # 8 = 1000, 7 = 0111, 8 & 7 = 0000

# Contar bits setados (population count)
def count_bits(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)  # Remove o bit mais a direita
    return count
# Ou use: bin(n).count('1')

# XOR para encontrar unico elemento (todos outros aparecem 2x)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # x ^ x = 0, x ^ 0 = x
    return result
```

### Propriedades importantes do XOR

```
x ^ 0 = x        (identidade)
x ^ x = 0        (auto-cancelamento)
x ^ y = y ^ x    (comutativo)
(x ^ y) ^ z = x ^ (y ^ z)  (associativo)
```

### Problemas classicos

1. **Single Number**: XOR de todos encontra o unico
2. **Number of 1 Bits**: `n & (n-1)` remove ultimo bit setado
3. **Power of Two**: `n & (n-1) == 0`
4. **Missing Number**: XOR de 0..n com array encontra o faltante
5. **Reverse Bits**: Shift e construir resultado
6. **Swap sem temp**: `a ^= b; b ^= a; a ^= b` (mais curiosidade que pratica)

### Quando usar bit manipulation

- Quando o problema menciona "sem espaco extra" ou O(1) espaco
- Problemas com conjuntos/subsets (cada bit = um elemento)
- Quando precisa de operacoes muito rapidas
- Flags e permissoes (bitmasks)

---

## 13. Matematica e Puzzles Logicos

### Conceitos numericos importantes

```python
# Verificar primo
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:  # So precisa checar ate sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Crivo de Eratostenes - todos os primos ate n
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

# GCD (Maximo Divisor Comum) - Algoritmo de Euclides
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# Ou use: from math import gcd

# LCM (Minimo Multiplo Comum)
def lcm(a, b):
    return a * b // gcd(a, b)
```

### Probabilidade e contagem

```python
# Fatorial
from math import factorial
# factorial(5) = 120

# Combinacao C(n, k) = n! / (k! * (n-k)!)
from math import comb
# comb(10, 3) = 120

# Permutacao P(n, k) = n! / (n-k)!
from math import perm
# perm(10, 3) = 720
```

### Puzzles logicos comuns

1. **Portas e Interruptores**: Pense em cada tentativa como ganhando informacao
2. **Pesagem (balanca)**: Divida em 3 grupos, nao 2
3. **Probabilidade**: Quebre em eventos simples, use arvore de decisao
4. **Dominos no tabuleiro**: Pense em coloracao (xadrez)
5. **Agua nos baldes**: Problemas de GCD (voce pode medir GCD(balde1, balde2) litros)

### Dica para puzzles

- **Nao entre em panico** - O entrevistador quer ver seu raciocinio
- **Comece com casos simples** - Resolva para n=1, n=2, n=3, procure padrao
- **Use contradicao** - Se parece impossivel, tente provar que e impossivel
- **Pense em invariantes** - O que nao muda em cada etapa?

---

## 14. Design Orientado a Objetos

### Abordagem para problemas de OOD

1. **Esclarecer requisitos**: O que o sistema faz? Quais as restricoes?
2. **Definir classes principais**: Quais sao os objetos do dominio?
3. **Definir relacionamentos**: Heranca, composicao, associacao
4. **Definir metodos**: Quais acoes cada objeto realiza?
5. **Considerar design patterns**: Factory, Singleton, Observer, Strategy

### Principios SOLID

```
S - Single Responsibility: Uma classe, uma responsabilidade
O - Open/Closed: Aberto para extensao, fechado para modificacao
L - Liskov Substitution: Subclasses substituem superclasses
I - Interface Segregation: Interfaces especificas > interfaces gerais
D - Dependency Inversion: Dependa de abstracoes, nao de implementacoes
```

### Design Patterns mais importantes

```python
# SINGLETON - Uma unica instancia
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# FACTORY - Criar objetos sem especificar a classe exata
class AnimalFactory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

# OBSERVER - Notificar multiplos objetos sobre mudancas
class EventEmitter:
    def __init__(self):
        self._listeners = defaultdict(list)

    def on(self, event, callback):
        self._listeners[event].append(callback)

    def emit(self, event, data=None):
        for callback in self._listeners[event]:
            callback(data)

# STRATEGY - Trocar algoritmos em tempo de execucao
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy(data)

# Uso:
sorter = Sorter(strategy=sorted)  # Pode trocar a funcao
```

### Problemas classicos de OOD

1. **Deck de cartas**: Classes Card, Deck, Hand, Game
2. **Estacionamento**: ParkingLot, ParkingSpot, Vehicle (heranca: Car, Motorcycle, Bus)
3. **Chat system**: User, Message, Conversation, ChatServer
4. **Sistema de arquivos**: File, Directory (composite pattern), FileSystem
5. **Jukebox**: Song, Playlist, Queue, Player

### Dica para candidatos experientes

Voce tem vantagem aqui! Use sua experiencia de arquitetura:
- Mencione **trade-offs** reais que voce ja enfrentou
- Discuta **extensibilidade** e **manutenibilidade**
- Mostre que pensa em **producao** (logging, error handling, testing)

---

## 15. Recursao e Programacao Dinamica

### Recursao - Fundamentos

```python
# Template de recursao
def solve(params):
    # 1. Caso base - SEMPRE defina primeiro!
    if base_case:
        return base_result

    # 2. Caso recursivo - quebre em subproblema menor
    return combine(solve(smaller_params))

# Exemplo: Fibonacci recursivo (ineficiente!)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
# Complexidade: O(2^n) tempo, O(n) espaco (call stack)
```

### Programacao Dinamica (DP)

DP e recursao + **cache de resultados**. Aplica-se quando:
1. **Subproblemas sobrepostos** (mesmos subproblemas calculados varias vezes)
2. **Subestrutura otima** (solucao otima = combinacao de solucoes otimas de subproblemas)

#### Top-Down (Memoization)

```python
# Fibonacci com memoization - O(n) tempo e espaco
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Usando @lru_cache (Python built-in - MUITO util em entrevistas!)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n-1) + fib_cached(n-2)
```

#### Bottom-Up (Tabulation)

```python
# Fibonacci bottom-up - O(n) tempo, O(n) espaco
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Otimizado - O(n) tempo, O(1) espaco
def fib_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
```

### Problemas classicos de DP

#### Climbing Stairs (variacao de Fibonacci)

```python
# Quantas formas de subir n degraus, pulando 1 ou 2 por vez?
@lru_cache(maxsize=None)
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)
```

#### 0/1 Knapsack

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # Nao inclui item i
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                              dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]
```

#### Longest Common Subsequence

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

#### Coin Change

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

### Como identificar problemas de DP

Procure estas pistas:
- "Quantas formas de..."
- "Minimo/maximo de..."
- "E possivel..."
- "Caminho mais curto/longo"
- Escolhas em cada passo afetam opcoes futuras
- O problema pode ser quebrado em subproblemas menores

### Framework para resolver DP

1. **Defina o estado**: O que `dp[i]` (ou `dp[i][j]`) representa?
2. **Encontre a relacao de recorrencia**: Como `dp[i]` se relaciona com estados anteriores?
3. **Defina o caso base**: `dp[0]`, `dp[1]`, etc.
4. **Determine a ordem de computacao**: Bottom-up ou top-down?
5. **Otimize espaco se possivel**: Precisa de toda a tabela ou so da ultima linha?

---

## 16. System Design e Escalabilidade

> **Sua area forte!** Use sua experiencia real aqui.

### Framework para System Design

#### 1. Entender requisitos (5 min)

```
Perguntas para fazer:
- Quem sao os usuarios? Quantos?
- Quais as funcionalidades principais? (MVP)
- Quais as restricoes? (latencia, disponibilidade, consistencia)
- Qual o volume de dados?
- Qual o trafego esperado? (QPS)
```

#### 2. Estimativas de capacidade (5 min)

```
Numeros uteis para ter na cabeca:
- 1 dia = ~100K segundos
- 1M usuarios, cada um fazendo 10 requests/dia = ~100 QPS
- 1 bilhao de requests/dia = ~12K QPS
- 1 MB de dados por usuario, 100M usuarios = 100 TB
```

#### 3. API Design (5 min)

Defina as APIs principais:
```
POST /api/v1/tweets
  body: { user_id, content, media_ids }
  response: { tweet_id, created_at }

GET /api/v1/feed?user_id=123&page=1
  response: { tweets: [...], next_page }
```

#### 4. Data Model (5 min)

```
Users: user_id (PK), username, email, created_at
Tweets: tweet_id (PK), user_id (FK), content, created_at
Follows: follower_id, followee_id, created_at
```

#### 5. Desenho do sistema de alto nivel (10 min)

Componentes tipicos:
- **Load Balancer** -> **Web Servers** -> **Application Servers**
- **Cache** (Redis/Memcached)
- **Database** (SQL/NoSQL)
- **Message Queue** (Kafka/RabbitMQ)
- **CDN** para conteudo estatico
- **Search** (Elasticsearch)

#### 6. Deep dive (10 min)

O entrevistador vai pedir para aprofundar em areas especificas.

### Conceitos fundamentais

#### Escalabilidade

```
Vertical Scaling: Maquina maior (limite fisico)
Horizontal Scaling: Mais maquinas (mais complexo, mas sem limite)

Regra geral: Comece vertical, escale horizontalmente quando necessario
```

#### Load Balancing

```
Algoritmos:
- Round Robin: Distribui igualmente (simples)
- Least Connections: Envia para quem tem menos conexoes
- IP Hash: Mesmo IP vai para mesmo servidor (sessoes)
- Weighted: Servidores mais potentes recebem mais
```

#### Caching

```python
# Estrategias de cache
# 1. Cache-Aside (Lazy Loading)
def get_user(user_id):
    # Tenta cache primeiro
    user = cache.get(f"user:{user_id}")
    if user:
        return user
    # Cache miss - busca no DB
    user = db.query(f"SELECT * FROM users WHERE id = {user_id}")
    cache.set(f"user:{user_id}", user, ttl=3600)
    return user

# 2. Write-Through: Escreve no cache E no DB simultaneamente
# 3. Write-Behind: Escreve no cache, DB atualizado assincronamente
# 4. Read-Through: Cache busca do DB automaticamente no miss

# Eviction policies:
# LRU (Least Recently Used) - mais comum
# LFU (Least Frequently Used)
# TTL (Time To Live) - expira apos tempo
```

#### Database Sharding

```
Estrategias:
- Range-based: user_id 1-1M -> shard1, 1M-2M -> shard2
  Problema: hot spots se distribuicao nao e uniforme

- Hash-based: shard = hash(user_id) % num_shards
  Problema: resharding e doloroso

- Directory-based: Lookup service mapeia chave -> shard
  Mais flexivel, mas lookup service e SPOF

Consistent Hashing: Minimiza realocacao quando shards sao adicionados/removidos
```

#### SQL vs NoSQL

| Aspecto | SQL | NoSQL |
|---------|-----|-------|
| Modelo | Tabelas relacionais | Documento, key-value, grafo |
| Schema | Rigido, definido antecipadamente | Flexivel, schema-less |
| Escalabilidade | Vertical (primariamente) | Horizontal (projetado para) |
| Transacoes | ACID completo | Eventual consistency (geralmente) |
| Joins | Suportado nativamente | Nao suportado / caro |
| Exemplos | PostgreSQL, MySQL | MongoDB, DynamoDB, Cassandra |
| Quando usar | Dados estruturados, relacoes complexas | Alto volume, schema flexivel, escala |

#### CAP Theorem

```
Voce so pode ter 2 de 3:
- Consistency (todos os nos veem os mesmos dados)
- Availability (toda request recebe resposta)
- Partition Tolerance (sistema funciona com falhas de rede)

Na pratica, P e inevitavel em sistemas distribuidos.
Entao a escolha real e: CP ou AP

CP: Consistencia forte (ex: bancos, transacoes financeiras)
AP: Alta disponibilidade (ex: redes sociais, feeds)
```

#### Message Queues

```
Quando usar:
- Processamento assincrono
- Desacoplar servicos
- Lidar com picos de trafego (buffer)
- Garantir processamento (at-least-once, exactly-once)

Ferramentas: Kafka (streaming), RabbitMQ (messaging), SQS (AWS)
```

### Problemas classicos de System Design

1. **URL Shortener**: Hashing, base62, database, cache, analytics
2. **Twitter Feed**: Fan-out on read vs write, cache, timeline service
3. **Chat System**: WebSockets, message queue, presence service
4. **Rate Limiter**: Token bucket, sliding window, Redis
5. **Notification System**: Push vs pull, priority queue, templating
6. **Search Autocomplete**: Trie, ranking, cache
7. **File Storage (Dropbox)**: Chunking, dedup, sync, metadata DB
8. **Video Streaming (YouTube)**: CDN, transcoding, upload pipeline

---

## 17. Sorting e Searching

### Algoritmos de Sorting

| Algoritmo | Tempo (melhor) | Tempo (medio) | Tempo (pior) | Espaco | Estavel? |
|-----------|---------------|---------------|-------------|--------|----------|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Sim |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Nao |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Sim |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | **O(n)** | Sim |
| **Quick Sort** | O(n log n) | O(n log n) | **O(n^2)** | O(log n) | Nao |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | Nao |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Sim |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Sim |

**Para entrevistas, foque em Merge Sort e Quick Sort.**

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Quando usar Merge Sort**: Quando precisa de estabilidade ou complexidade garantida O(n log n). Bom para linked lists (merge in-place sem espaco extra).

### Quick Sort

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Escolhe ultimo como pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Quando usar Quick Sort**: Melhor performance na pratica (cache-friendly), in-place. Python usa **Timsort** internamente (hibrido de merge sort + insertion sort).

### Binary Search

```python
# Template basico - MEMORIZE
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Evita overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Nao encontrado

# Variacao: encontrar primeira ocorrencia
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continua buscando a esquerda
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Binary search em resposta (search space)
# "Qual o minimo/maximo valor X tal que condicao(X) e verdadeira?"
def binary_search_answer(low, high, condition):
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

### Problemas classicos

1. **Search in Rotated Sorted Array**: Binary search modificado
2. **Find Peak Element**: Binary search comparando com vizinhos
3. **Merge Intervals**: Sort por inicio, merge sobrepostos
4. **Kth Largest Element**: Quick select O(n) medio ou heap O(n log k)
5. **Sort Colors (Dutch Flag)**: Three-way partition
6. **Meeting Rooms**: Sort + checar sobreposicao

### Quick Select (Kth elemento)

```python
import random

def quick_select(arr, k):
    """Encontra o k-esimo menor elemento. O(n) medio."""
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))
```

---

## 18. Testing

### Abordagem para perguntas de testing

O CTCI aborda testing como uma habilidade de entrevista, nao apenas tecnica.

#### Framework para testar qualquer coisa

1. **Entenda o que esta testando**: Software? Hardware? Funcao?
2. **Quem vai usar?**: Diferentes usuarios = diferentes testes
3. **Quais os casos de uso?**: Fluxos principais
4. **Quais os limites?**: Boundary conditions
5. **Quais as condicoes de falha?**: O que pode dar errado?

#### Categorias de teste

```
Testes Funcionais:
- Casos normais (happy path)
- Edge cases (limites, vazios, nulos)
- Casos invalidos (input errado)
- Casos de erro (o que acontece quando falha?)

Testes Nao-Funcionais:
- Performance (carrega em tempo aceitavel?)
- Seguranca (resiste a ataques?)
- Usabilidade (usuario consegue usar?)
- Escalabilidade (funciona com 10x usuarios?)
```

#### Testando funcoes de codigo

```python
# Para testar uma funcao sort():
def test_sort():
    # Caso normal
    assert sort([3, 1, 2]) == [1, 2, 3]

    # Array vazio
    assert sort([]) == []

    # Um elemento
    assert sort([1]) == [1]

    # Ja ordenado
    assert sort([1, 2, 3]) == [1, 2, 3]

    # Ordem reversa
    assert sort([3, 2, 1]) == [1, 2, 3]

    # Duplicados
    assert sort([2, 1, 2, 1]) == [1, 1, 2, 2]

    # Todos iguais
    assert sort([5, 5, 5]) == [5, 5, 5]

    # Negativos
    assert sort([-1, 3, -2]) == [-2, -1, 3]

    # Array grande
    import random
    big = random.sample(range(10000), 10000)
    assert sort(big) == sorted(big)
```

#### Dica de entrevista sobre testing

Quando voce apresentar sua solucao de codigo, **teste proativamente** antes que o entrevistador peca. Isso demonstra maturidade e rigor profissional.

---

## 19. Databases e SQL

### Conceitos fundamentais

#### Normalizacao

```
1NF: Valores atomicos, sem repeticao de grupos
2NF: 1NF + sem dependencias parciais (toda coluna depende da PK inteira)
3NF: 2NF + sem dependencias transitivas

Exemplo de desnormalizacao proposital:
- Armazenar nome_do_usuario na tabela de pedidos (evita JOIN)
- Trade-off: redundancia vs performance de leitura
```

#### JOINs - Os 4 tipos essenciais

```sql
-- INNER JOIN: So registros com match em ambas tabelas
SELECT u.name, o.order_id
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: Todos de users + match de orders (NULL se nao tem)
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN: Todos de orders + match de users
SELECT u.name, o.order_id
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN: Todos de ambas
SELECT u.name, o.order_id
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;
```

#### Queries comuns em entrevistas

```sql
-- Top N por grupo (Window Function)
SELECT *
FROM (
    SELECT
        department,
        name,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn <= 3;

-- Segundo maior salario
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Duplicados
SELECT email, COUNT(*) as cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Auto-join: empregados que ganham mais que seu gerente
SELECT e.name as employee
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- Pivot / Agregacao condicional
SELECT
    department,
    COUNT(*) as total,
    SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as active,
    AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

#### Indices

```
O que sao: Estrutura de dados (geralmente B-tree) que acelera buscas
Quando usar: Colunas frequentemente usadas em WHERE, JOIN, ORDER BY
Trade-off: Acelera leituras, desacelera escritas (precisa atualizar indice)
Tipos: B-tree (geral), Hash (igualdade), GiST (espacial), GIN (full-text)

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);  -- Composto
```

#### ACID

```
A - Atomicidade: Transacao e tudo ou nada
C - Consistencia: Dados sempre em estado valido
I - Isolamento: Transacoes nao interferem entre si
D - Durabilidade: Dados commitados sobrevivem a falhas
```

---

## 20. Threads e Locks

### Conceitos fundamentais

```python
import threading

# Thread basica
def worker(name):
    print(f"Thread {name} executando")

t = threading.Thread(target=worker, args=("A",))
t.start()
t.join()  # Espera terminar
```

### Mutex (Lock)

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Adquire e libera automaticamente
            counter += 1

# Sem lock, counter pode ser < 200000 (race condition!)
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)  # Com lock: sempre 200000
```

### Deadlock

Ocorre quando duas ou mais threads ficam esperando recursos que as outras seguram.

```python
# DEADLOCK - NAO FACA ISSO
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1():
    lock_a.acquire()
    # ... faz algo ...
    lock_b.acquire()  # Espera lock_b, que thread2 segura
    lock_b.release()
    lock_a.release()

def thread2():
    lock_b.acquire()
    # ... faz algo ...
    lock_a.acquire()  # Espera lock_a, que thread1 segura -> DEADLOCK!
    lock_a.release()
    lock_b.release()
```

### Condicoes para Deadlock (todas devem ser verdadeiras)

1. **Exclusao mutua**: Recurso so pode ser usado por uma thread
2. **Hold and wait**: Thread segura recurso enquanto espera outro
3. **Sem preempcao**: Recursos nao podem ser forcadamente removidos
4. **Espera circular**: A espera B, B espera A

### Como prevenir Deadlock

```python
# Solucao 1: Ordenar locks (sempre adquirir na mesma ordem)
def safe_thread1():
    lock_a.acquire()  # Sempre A primeiro, depois B
    lock_b.acquire()
    # ...
    lock_b.release()
    lock_a.release()

def safe_thread2():
    lock_a.acquire()  # Mesma ordem!
    lock_b.acquire()
    # ...
    lock_b.release()
    lock_a.release()

# Solucao 2: Timeout
if lock_a.acquire(timeout=5):
    if lock_b.acquire(timeout=5):
        # ...
        lock_b.release()
    lock_a.release()
```

### Semaphore

```python
# Limita numero de threads simultaneas
semaphore = threading.Semaphore(3)  # Maximo 3 threads

def limited_worker(name):
    with semaphore:  # So 3 podem executar ao mesmo tempo
        print(f"Thread {name} trabalhando")
        import time; time.sleep(1)
```

### Python e o GIL

```
GIL (Global Interpreter Lock):
- Python (CPython) tem um lock global que permite apenas 1 thread executar
  codigo Python por vez
- Threads sao uteis para I/O-bound (rede, disco) mas NAO para CPU-bound
- Para CPU-bound, use multiprocessing (processos separados)

import multiprocessing
# Cada processo tem seu proprio GIL
p = multiprocessing.Process(target=worker, args=("A",))
```

### Producer-Consumer (padrao classico)

```python
import threading
from collections import deque

class BoundedBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def produce(self, item):
        with self.not_full:
            while len(self.buffer) == self.buffer.maxlen:
                self.not_full.wait()  # Espera ate ter espaco
            self.buffer.append(item)
            self.not_empty.notify()  # Avisa consumer

    def consume(self):
        with self.not_empty:
            while len(self.buffer) == 0:
                self.not_empty.wait()  # Espera ate ter item
            item = self.buffer.popleft()
            self.not_full.notify()  # Avisa producer
            return item
```

---

## 21. Padroes Comuns de Entrevista

### Os 10 padroes mais importantes

#### 1. Two Pointers

**Quando usar**: Array ordenado, encontrar pares, particionar

```python
# Pair com soma alvo em array ordenado
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []

# Container With Most Water
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water
```

#### 2. Sliding Window

**Quando usar**: Subarray/substring contiguo, tamanho fixo ou variavel

```python
# Janela de tamanho variavel: menor subarray com soma >= target
def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0

# Longest substring sem caracteres repetidos
def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

#### 3. BFS (Breadth-First Search)

**Quando usar**: Menor caminho, busca por niveis, grafos nao ponderados

```python
# Numero de ilhas (grid)
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1

    return count
```

#### 4. DFS (Depth-First Search)

**Quando usar**: Explorar todos os caminhos, detectar ciclos, backtracking

```python
# Todas as permutacoes
def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()  # Backtrack!

    backtrack([], nums)
    return result

# Todos os subsets
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

#### 5. Binary Search

**Quando usar**: Array ordenado, search space monotono, otimizacao min/max

```python
# Search in Rotated Sorted Array
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Metade esquerda e ordenada
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Metade direita e ordenada
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

#### 6. Dynamic Programming

**Quando usar**: Contagem de formas, otimizacao, subproblemas sobrepostos

(Ver secao 15 para exemplos detalhados)

#### 7. Greedy

**Quando usar**: Escolha local otima leva a solucao global otima

```python
# Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged

# Jump Game
def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True
```

#### 8. Hash Map

**Quando usar**: Lookup O(1), contagem, mapeamento, deduplicacao

```python
# Group Anagrams
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Subarray Sum Equals K (prefix sum + hash map)
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Soma 0 aparece 1 vez (antes do inicio)

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count
```

#### 9. Stack

**Quando usar**: Matching de pares, expressoes, proximo maior/menor

(Ver secao 10 para exemplos detalhados)

#### 10. Prefix Sum

**Quando usar**: Soma de subarray, consultas de range

```python
# Range Sum Query
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

# Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Prefix product (esquerda para direita)
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Suffix product (direita para esquerda)
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
```

### Como identificar o padrao correto

```
Array ordenado?                     -> Two Pointers ou Binary Search
Subarray/substring contiguos?       -> Sliding Window
Menor caminho em grafo?             -> BFS
Explorar todos os caminhos?         -> DFS/Backtracking
Contagem / otimizacao com choices?  -> DP
Escolha local = global?             -> Greedy
Lookup rapido?                      -> Hash Map
Matching / ordem reversa?           -> Stack
Soma de ranges?                     -> Prefix Sum
Elementos extremos (min/max)?       -> Heap
Componentes conectados?             -> Union-Find
Prefixos de strings?                -> Trie
```

---

## 22. Dicas e Estrategias

### O que fazer quando estiver travado

1. **Fale em voz alta**: "Estou pensando em... mas nao tenho certeza se..."
2. **Volte ao exemplo**: Resolva manualmente e observe o que voce faz
3. **Simplifique o problema**: Resolva uma versao mais facil primeiro
4. **Pense em estruturas de dados**: "E se eu usasse um hash map aqui?"
5. **Pense em padroes**: "Isso parece um problema de sliding window..."
6. **Brute force primeiro**: Qualquer solucao e melhor que nenhuma
7. **Como ultimo recurso, peca uma dica**: "Estou travado, pode me dar uma direcao?"

### Como comunicar durante a entrevista

#### DO (Faca isso)

- **Pense em voz alta** desde o inicio
- **Pergunte antes de codar**: "Minha abordagem e X, faz sentido continuar?"
- **Declare trade-offs**: "Posso otimizar tempo mas vai custar O(n) espaco"
- **Admita quando nao sabe**: "Nao tenho certeza sobre X, mas minha intuicao e..."
- **Teste seu codigo**: Percorra com um exemplo

#### DON'T (Evite isso)

- Ficar em silencio por mais de 30 segundos
- Comecar a codar imediatamente sem pensar
- Ignorar hints do entrevistador
- Dizer "eu sei isso" e dar resposta sem explicar
- Ficar defensivo quando apontam um bug

### Checklist pre-entrevista

```
[ ] Revisei estruturas de dados fundamentais
[ ] Pratiquei pelo menos 50 problemas variados
[ ] Fiz mock interviews (pelo menos 2-3)
[ ] Preparei 5-6 historias comportamentais (STAR)
[ ] Preparei perguntas para fazer ao entrevistador
[ ] Revisei system design (para posicao senior/staff)
[ ] Teste meu setup tecnico (camera, microfone, IDE)
[ ] Descansei na vespera
```

### Erros mais comuns

| Erro | Solucao |
|------|---------|
| Comecar a codar sem pensar | Siga os 7 passos |
| Nao testar edge cases | Sempre teste: vazio, 1 elemento, negativo |
| Solucao over-engineered | Comece simples, otimize depois |
| Nao comunicar | Pense em voz alta SEMPRE |
| Ignorar complexidade | Declare Big O de tempo E espaco |
| Codigo ilegivel | Nomes claros, funcoes auxiliares |
| Nao tratar erros | Null checks, bounds checking |

### Estrategia especifica para voce (ex-gestor, 10 anos)

1. **Suas forcas**: System design, comunicacao, visao de producao. USE ISSO.
2. **Seu desafio**: Coding pode estar enferrujado. PRATIQUE DIARIAMENTE.
3. **Sua vantagem**: Voce pensa em trade-offs naturalmente. Mencione isso.
4. **Sua historia**: "Voltando para hands-on porque amo construir". Seja genuino.
5. **Tempo de pratica**: 2-3 problemas por dia, focando em padroes, nao em quantidade
6. **Mock interviews**: Faca pelo menos 3-5 antes da entrevista real

### Recursos complementares

- **LeetCode**: Problemas por padrao e dificuldade
- **NeetCode.io**: Videos explicativos, roadmap de 150 problemas
- **System Design Primer** (GitHub): Referencia completa de system design
- **Tech Interview Handbook**: Cheatsheets por topico
- **Pramp / Interviewing.io**: Mock interviews com outras pessoas

---

## Referencia Rapida: Complexidade de Operacoes

### Estruturas de Dados

| Estrutura | Acesso | Busca | Insercao | Remocao | Espaco |
|-----------|--------|-------|----------|---------|--------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | - | O(1)** | O(1)** | O(1)** | O(n) |
| BST (balanceado) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | - | O(n) | O(log n) | O(log n) | O(n) |
| Trie | - | O(m) | O(m) | O(m) | O(n*m) |

*Com ponteiro para o no | **Amortizado, pior caso O(n) | m = tamanho da chave

### Algoritmos de Sorting

| Algoritmo | Melhor | Medio | Pior | Espaco | Estavel |
|-----------|--------|-------|------|--------|---------|
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | Nao |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Sim |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | Nao |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Sim |

### Grafos

| Algoritmo | Tempo | Espaco | Uso |
|-----------|-------|--------|-----|
| BFS | O(V+E) | O(V) | Menor caminho (nao ponderado) |
| DFS | O(V+E) | O(V) | Ciclos, caminhos, topological |
| Dijkstra | O(E log V) | O(V) | Menor caminho (ponderado) |
| Topological Sort | O(V+E) | O(V) | Ordenacao de dependencias |
| Union-Find | O(alpha(n)) | O(n) | Componentes conectados |

---

*Documento compilado em fevereiro de 2026 como referencia de estudo para entrevistas tecnicas.*
*Baseado em "Cracking the Coding Interview" (6a ed.) por Gayle Laakmann McDowell.*