class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        diag_map = {}
        for x in range(-(m - 1), n):
            diag_map[x] = []

        for i in range(n):
            for j in range(m):
                diag_map[i - j].append(mat[i][j])

        for x in diag_map:
            heapq.heapify(diag_map[x])

        for i in range(n):
            for j in range(m):
                mat[i][j] = heapq.heappop(diag_map[i - j])

        return mat

