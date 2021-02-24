class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        ci = 0
        ri = n - 1

        while (ci < m and ri >= 0):
            if matrix[ri][ci] > target:
                ri -= 1

            elif matrix[ri][ci] < target:
                ci += 1

            else:
                return True

        return False