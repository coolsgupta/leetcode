import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i, row in enumerate(mat):
            heapq.heappush(heap, (sum(row), i))

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
