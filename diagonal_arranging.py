def get_rows(grid):
    return [[c for c in r] for r in grid]

def get_cols(grid):
    return zip(*grid)

def get_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]


def diagonalsArranging(a):
    diagonals = get_diagonals(a)
    cyclic_diagonals = []
    d_map = {}
    for i, diagonal in enumerate(diagonals):
        inc = len(a)//len(diagonal) + 1
        cycle = diagonal*inc
        cycle = ''.join(cycle[:len(a)])
        cyclic_diagonals.append(''.join(cycle))
        if cycle not in d_map:
            d_map[cycle] = []
        d_map[cycle].append(i+1)

    cyclic_diagonals = sorted(cyclic_diagonals)

    indices = []
    for i in range(len(cyclic_diagonals)):
        if cyclic_diagonals[i] == cyclic_diagonals[i-1]:
            continue
        indices.extend(sorted(d_map.get(cyclic_diagonals[i])))

    return indices

a = [[ "a", "c", "a", "b", "b"],
[ "c", "b", "a", "c", "b"],
[ "a", "a", "e", "c", "b"],
[ "b", "b", "d", "a", "g"],
[ "a", "b", "e", "b", "a"]]

ans = diagonalsArranging(a)

