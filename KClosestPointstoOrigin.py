class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for x in points:
            if len(res) < K:
                heapq.heappush(res, (-(x[0] ** 2 + x[1] ** 2), x));
            else:
                dist = -(x[0] ** 2 + x[1] ** 2)
                if dist > res[0][0]:
                    heapq.heappushpop(res, (dist, x))

        soln = [x[1] for x in res]

        return soln
