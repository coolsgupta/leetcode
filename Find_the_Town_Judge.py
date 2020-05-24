class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {}
        if N == 1:
            return 1

        for x in trust:
            if x[0] not in d:
                d[x[0]] = [0, 0]
            if x[1] not in d:
                d[x[1]] = [0, 0]
            d[x[0]][0] += 1
            d[x[1]][1] += 1

        for x in d:
            if d[x][0] == 0 and d[x][1] == N - 1:
                return x
        return -1

Solution().findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])