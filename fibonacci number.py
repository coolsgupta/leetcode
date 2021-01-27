class Solution:
    def fib(self, n: int) -> int:
        x = 0
        y = 1
        c = 1

        for _ in range(n):
            c = x + y
            x, y = y, c

        return x