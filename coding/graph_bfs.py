grids = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],n
    [0, 0, 0, 1, 1]
]
island = {}
for grid in grids:
    count = 0
    for g in grid:
        if g not in island:
            island[g] = count
        count += 1