class Solution:
    def tribonacci(self, n: int) -> int:
        tn = [0, 1, 1]

        if n < 3:
            return tn[n]

        for _ in range(2, n):
            tn = [tn[1], tn[2], sum(tn)]

        return tn[2]
