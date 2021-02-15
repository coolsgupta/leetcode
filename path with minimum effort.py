class Solution:
    def get_child(self, point):
        children = []
        for a in self.actions:
            child = (point[0] + a[0], point[1] + a[1])
            if 0 <= child[0] <= self.n and 0 <= child[1] <= self.m:
                children.append(child)

        return children

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.n = len(heights) - 1
        self.m = len(heights[0]) - 1
        queue = [(0, (0, 0))]
        heapq.heapify(queue)
        visited = {
            (0, 0): 0
        }
        goal = (self.n, self.m)
        while (queue):
            eff, curr = heapq.heappop(queue)
            if curr == goal:
                return eff

            children = self.get_child(curr)
            for child in children:
                child_eff = abs(heights[curr[0]][curr[1]] - heights[child[0]][child[1]])
                if child not in visited or child_eff < visited[child]:
                    visited[child] = child_eff
                    heapq.heappush(queue, (max(child_eff, eff), child))
