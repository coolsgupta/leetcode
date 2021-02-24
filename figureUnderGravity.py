def figureUnderGravity(matrix):
    n, m = len(matrix), len(matrix[0])
    res = [['.']*m for _ in range(n)]
    for i in range(m):
        s = []
        flag = False
        for j in range(n-1, -1, -1):
            if matrix[j][i] == 'F':
                while (len(s) > 1 and s[-1] == '.'):
                    s.pop()
            flag = True

            s.append(matrix[j][i])
            while (len(s) < n - j):
                s.append('.')

        x = 1
        while(x <= len(s)):
            res[-x][i] = s[x-1]
            x += 1

    return res

if __name__ == '__main__':
    matrix = [["F", "F", "F"], ["#", ".", "."], ["F", "F", "F"], [".", "#", "."], ["#", "F", "F"], [".", ".", "."]]
    print(figureUnderGravity(matrix))