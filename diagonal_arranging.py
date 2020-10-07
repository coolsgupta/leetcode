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
    n = len(a)
    cyclic_diagonals = sorted([("".join((diag*(n//len(diag) + 1))[:n]), i) for i, diag in enumerate(diagonals)])
    return [x[1] + 1 for x in cyclic_diagonals]

a = [[ "a", "c", "a", "b", "b"],
[ "c", "b", "a", "c", "b"],
[ "a", "a", "e", "c", "b"],
[ "b", "b", "d", "a", "g"],
[ "a", "b", "e", "b", "a"]]

ans = diagonalsArranging(a)
print(ans)

