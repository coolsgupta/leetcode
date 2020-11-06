class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for x in logs:
            if x == '../':
                c = c - 1 if c > 0 else 0
            elif x == './':
                pass
            else:
                c += 1
        return c
