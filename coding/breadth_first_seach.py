from collections_counter import deque


def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # achou terra!
                count += 1  # ilha nova
                # BFS: pinta toda a ilha de 0
                queue = deque()
                queue.append((r, c))
                grid[r][c] = 0  # marca como visitado

                # 0 [1, 1, 0, 0],
                # 1 [1, 0, 0, 1],
                # 2 [0, 0, 1, 1],
                # 3 [0, 0, 0, 0]

                while queue:
                    row, col = queue.popleft()
                    for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = row + drow, col + dcol
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))

    return count


grids = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

result = count_islands(grids)
print(result)
