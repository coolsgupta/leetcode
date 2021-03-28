from typing import *

class Solution:
    # def getColumn(self, col):
    #     # x, y = 0, col
    #     # while x < self.n:
    #     #     if self.grid[x][y] == -1:
    #     #         if y == 0:
    #     #             return -1
    #     #
    #     #         if self.grid[x][y - 1] == 1:
    #     #             return -1
    #     #
    #     #         x += 1
    #     #         y -= 1
    #     #
    #     #     elif self.grid[x][y] == 1:
    #     #         if y == self.m - 1:
    #     #             return -1
    #     #
    #     #         if self.grid[x][y + 1] == -1:
    #     #             return -1
    #     #
    #     #         x += 1
    #     #         y += 1
    #     x, y = 0, col
    #     while x < self.n:
    #         new_y = y + self.grid[x][y]
    #         if 0 <= new_y < self.m and self.grid[x][new_y] == self.grid[x][y]:
    #             y = new_y
    #             x += 1
    #
    #         else:
    #             return -1
    #
    #     return y
    #
    # def findBall(self, grid: List[List[int]]) -> List[int]:
    #     self.grid = grid
    #     self.n = len(grid)
    #     self.m = len(grid[0])
    #     arr = [self.getColumn(i) for i in range(self.m)]
    #     return arr
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # self.grid = grid
        n = len(grid)
        m = len(grid[0])
        arr = [-1] * m

        for i in range(m):
            x, y = 0, i
            while x < n:
                new_y = y + grid[x][y]
                if 0 <= new_y < m and grid[x][new_y] == grid[x][y]:
                    y = new_y
                    x += 1

                else:
                    arr[i] = -1
                    break
            else:
                arr[i] = y

        return arr


if __name__ == '__main__':
    case = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    res = Solution().findBall(case)
    print(res)
