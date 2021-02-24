def backtrack (so_far, word, grid, i, j, coo):
    if so_far == word:
        return coo

    if i >= len(grid) or j >= len(grid[0]):
        return None

    so_far = so_far + grid[i][j]
    if so_far != word[:len(so_far)]:
        return None

    return backtrack (so_far, word, grid, i + 1, j, coo + [(i, j)]) or backtrack (so_far, word, grid, i, j + 1, coo + [(i, j)])


def findWord(word, grid):
    flag = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                flag = backtrack(word[0], word, grid, i + 1, j, [(i, j)]) or backtrack(word[0], word, grid, i, j + 1, [(i, j)])
                if flag:
                    break

    return flag

if __name__ == '__main__':
    case = [['c','r','c','a','r','s'],['a','b','i','t','n','b'], ['t','f','n','n','t','i'], ['x','s','i','i','p','t']]
    res = findWord('catnip', case)
    print(res)