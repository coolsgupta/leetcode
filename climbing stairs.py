class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        c = 1

        for i in range(0, n):
            c = x + y
            x, y = y, c

        return c

