def get_elem(x,y, matrix):
    if x < 0 or y < 0:
        return 0
    return matrix[x][y]


def findBeforeMatrix(after):
    before = []
    for x in range(len(after)):
        before.append([])
        for y in range(len(after[0])):
            element = get_elem(x, y, after) - get_elem(x-1, y, after) - get_elem(x, y-1, after)+ get_elem(x-1, y-1, after)
            before[x].append(element)

    return before

after = [[2, 5], [7, 17]]
ans = findBeforeMatrix(after)
print(ans)
