class Solution:
    def __init__(self):
        self.curr_size = 0

    def dfs(self, x, y, grid):
        if x < 0 or x > self.n - 1 or y < 0 or y > self.m - 1 or grid[x][y] == 0:
            return

        self.curr_size += 1

        grid[x][y] = 0
        if x - 1 >= 0:
            self.dfs(x - 1, y, grid)

        if y - 1 >= 0:
            self.dfs(x, y - 1, grid)

        if x + 1 < self.n:
            self.dfs(x + 1, y, grid)

        if y + 1 < self.m:
            self.dfs(x, y + 1, grid)

        if x - 1 >= 0 and y - 1 >= 0:
            self.dfs(x - 1, y - 1, grid)

        if x + 1 <= self.n  and y - 1 >= 0:
            self.dfs(x + 1, y - 1, grid)

        if x + 1 <= self.n  and y + 1 < self.m:
            self.dfs(x + 1, y + 1, grid)

        if x - 1 >= 0 and y + 1 < self.m:
            self.dfs(x - 1, y + 1, grid)

    def numIslands(self, grid):
        self.n = len(grid)
        self.m = len(grid[0])
        res = []

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid)
                    res.append(self.curr_size)
                    self.curr_size = 0

        return res


if __name__ == '__main__':
    case = [
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1]
    ]
    print(" ".join(Solution().numIslands(case)))


n, m = input().split(' ')
n = int(n)
m = int(m)
case = []
for _ in range(n):
    row = input()
    if row:
        case.append(row.split(' '))
