class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        if R * C == 1:
            return ans

        for k in range(1, 2 * (R + C), 2):
            for dr, dc, dk in [(0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)]:
                for _ in range(dk):
                    r0 += dr
                    c0 += dc
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans