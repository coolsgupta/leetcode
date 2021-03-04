size = int(raw_input())
matrix = [[0] * size for _ in range(size)]

for i in range(size):
    input = raw_input().split(' ')
    for j in range(size):
        matrix[j][size - i - 1] = str(input[j])

for row in matrix:
    print(' '.join(row))