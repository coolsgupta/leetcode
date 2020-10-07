def get_elem(x,y, matrix):
    if x < 0 or y < 0:
        return 0
    return matrix[x][y]


def findBeforeMatrix(after):
    # detailed response
    # before = []
    # for x in range(len(after)):
    #     before.append([])
    #     for y in range(len(after[0])):
    #         element = get_elem(x, y, after) - get_elem(x-1, y, after) - get_elem(x, y-1, after) + get_elem(x-1, y-1, after)
    #         before[x].append(element)

    # list comprehension version of response
    before = [
        [
            get_elem(i, j, after) - get_elem(i - 1, j, after) - get_elem(i, j - 1, after) + get_elem(i - 1, j - 1, after)
            for j in range(len(after[0]))
        ]
        for i in range(len(after))
    ]

    return before


if __name__ == '__main__':

after = [[2, 5], [7, 17]]
ans = findBeforeMatrix(after)
print(ans)
