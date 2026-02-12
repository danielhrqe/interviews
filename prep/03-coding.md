# Coding - Prep Guide

> Sources: [coding-roadmap.md](../coding-roadmap.md), [coding/*.py](../coding/), [ctci-knowledge-base.md](../ctci-knowledge-base.md), Feb 11 diagnostic

---

## 1. Platform & Format Quick Reference

| Company | Platform | Format | Duration | Language | Difficulty | Key Focus |
|---------|----------|--------|----------|----------|------------|-----------|
| **Nubank** | CodeSignal (GCA) | Solo, proctored, 4 Qs | 70 min | Any (Python ok) | Easy→Med-Hard | Arrays, strings, hashmap, sliding window |
| **QuintoAndar** | Codility | Solo | 1h | Any | Easy-Medium | Correctness + edge cases |
| **Wise** | HackerRank CodePair | Pair programming | 1h | Java preferred | Easy-Medium | Clean code, OOP, practical |
| **DoorDash** | HackerRank CodePair | Code Craft (rare for EM) | 45-60 min | Any | Medium-Hard | Clean code, classes, defensive |

**Nubank CodeSignal strategy**: Q1 → Q2 → **Q4** → Q3 (Q4 worth more per time invested)

---

## 2. Pattern Cheat Sheet (Skeleton Templates)

### HashMap (ALL companies)
```python
# Two Sum: find pair summing to target
def two_sum(nums, target):
    seen = {}  # val -> index
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
    return []

# Frequency count
from collections import Counter
freq = Counter(items)  # {item: count}
most_common = freq.most_common(3)  # top 3

# Group by key
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[key_func(item)].append(item)
```

### Two Pointers (QA, Wise, Nubank)
```python
# Sorted array: find pair with target sum
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

# Remove duplicates in-place (sorted array)
def remove_dupes(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

### Sliding Window (Nubank CodeSignal, QA, DD)
```python
# Fixed size: max sum of subarray of size k
def max_sum_k(arr, k):
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]  # slide: add new, remove old
        best = max(best, window)
    return best

# Variable size: longest substring without repeats
def longest_unique_substr(s):
    seen = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

### Binary Search (ALL)
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # not found
# Time: O(log n), Space: O(1)
```

### BFS Grid (DD, QA, Nubank CodeSignal)
```python
from collections import deque

def bfs_grid(grid, starts):
    """Multi-source BFS: find min distance from any start cell."""
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    for r, c in starts:
        dist[r][c] = 0
        queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1 and grid[nr][nc] != 'X':
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist
```

### Stack (ALL)
```python
# Valid parentheses
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0
```

### Sorting with key= (QA, Wise, Nubank)
```python
# Sort by custom key
intervals.sort(key=lambda x: x[0])          # by start time
words.sort(key=len)                           # by length
items.sort(key=lambda x: (-x[1], x[0]))     # by score desc, then name asc

# Max/min with key
longest = max(words, key=len)
most_frequent = max(freq, key=freq.get)      # key in dict with highest value
```

### Collections (Counter, defaultdict, deque)
```python
from collections import Counter, defaultdict, deque

# Counter
c = Counter([1, 2, 2, 3, 3, 3])  # {3: 3, 2: 2, 1: 1}
c.most_common(2)                   # [(3, 3), (2, 2)]
c['new'] += 1                      # safe, defaults to 0

# defaultdict
dd = defaultdict(list)             # missing key → empty list
dd = defaultdict(int)              # missing key → 0
dd = defaultdict(set)              # missing key → empty set

# deque (double-ended queue)
q = deque()
q.append(1)        # right end: O(1)
q.appendleft(0)    # left end: O(1)
q.pop()             # right end: O(1)
q.popleft()         # left end: O(1)
# NEVER use list.pop(0) — it's O(n)!
```

---

## 3. Company-Specific Gotchas

### Nubank
- **NO databases** — use in-memory collections (atoms, lists, dicts)
- Functional patterns preferred: `map()`, `filter()`, `reduce()`
- Clean code > algorithm complexity
- JSON stdin/stdout processing
- Penalty for: dead code, unnecessary comments, bad naming

### Wise
- **Java preferred** — confirm with recruiter, Python may be accepted
- OOP focus: SOLID principles, design patterns (circuit breaker, strategy)
- Concurrency basics: thread safety, ConcurrentHashMap concepts
- Pair programming: explain everything aloud, treat interviewer as collaborator
- Not LeetCode-style: practical, domain-relevant problems

### QuintoAndar (Codility)
- Focus on correctness + edge cases (Codility scores both)
- Practice on Codility demo before the real test
- Arrays, strings, sorting, hash maps, binary search

### DoorDash (if coding comes up)
- "Code Craft" format: collaborative, not pure algorithms
- Clean, testable, scalable code > optimal algorithm
- OOP: create classes, methods, good structure
- Defensive programming: input validation, error handling
- Domain-themed problems (delivery logistics, menus, grids)

---

## 4. Pre-Interview Checklist (30 min before)

- [ ] IDE/platform loaded and tested (HackerRank, CodeSignal, Codility)
- [ ] Python boilerplate ready: `from collections import Counter, defaultdict, deque`
- [ ] Webcam, mic, screen share tested
- [ ] Water, quiet room, phone silenced
- [ ] Quick mental review: "What pattern for what signal?"
  - Sorted array → Two Pointers / Binary Search
  - Subarray/substring → Sliding Window
  - Frequency/lookup → HashMap
  - Shortest path → BFS
  - Matching/nesting → Stack
- [ ] Remind yourself: brute force first, optimize second, talk the whole time

---

## 5. Weak Spots Quick Review (from Feb 11 diagnostic)

| Topic | Gap | Quick Fix |
|-------|-----|-----------|
| **Binary Search** | Didn't know before, learned concept | Practice: implement from memory 3x, then LC 704 + LC 33 |
| **BFS grid** | Didn't know BFS | Practice: implement multi-source BFS template, then LC 286/542 |
| **Collections** | Didn't know defaultdict/Counter | Memorize the 3 imports + usage patterns above |
| **Sliding Window** | Didn't know incremental trick | Practice: fixed-size (max sum k) + variable-size (longest unique) |
| **Two Pointers** | Didn't do in-place | Practice: remove dupes in-place, reverse in-place |
| **Stack** | Knows idea, can't implement | Practice: valid parentheses from memory |
| **Python copy/mutable** | Failed copy + mutable default args | Remember: `def f(x=[])` is shared! Use `def f(x=None): x = x or []` |
| **Sorting key=** | Didn't know `key=` param | Practice: `max(d, key=d.get)`, `sort(key=lambda x: x[1])` |
| **Big O** | Missed sort = O(n log n) | Review: sort=n log n, binary search=log n, BFS=V+E |
