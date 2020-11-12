class Solution:
    def dist(self, p1, p2):
        return sum([(x - y) ** 2 for x, y in zip(p1, p2)])

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False

        p = [p1, p2, p3, p4]
        dist = []
        for i in range(3):
            for j in range(i + 1, 4):
                dist.append(self.dist(p[i], p[j]))

        dist.sort()
        # print(dist)
        if dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5] and 2 * dist[1] == dist[4]:
            return True

        return False
