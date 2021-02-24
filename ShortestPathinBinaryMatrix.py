import heapq


class Solution:
    def get_child(self, point):
        children = []
        for dx, dy in self.actions:
            x = point[0] + dx;
            y = point[1] + dy;
            if 0 <= x < self.n and 0 <= y < self.n and self.grid[x][y] == 0:
                children.append((x, y))

        return children

    def get_h_val(self, point):
        dx = (self.n - 1 - point[0])
        dy = (self.n - 1 - point[1])
        return max(dx, dy)

    def shortestPathBinaryMatrix(self, grid):
        if (grid[0][0] == 0):
            self.actions = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (1, 0), (0, -1), (-1, 0)]
            self.n = len(grid)
            self.grid = grid
            self.adjacency_map = {
                (0, 0): [1, (-1, -1)]
            }
            queue = [(self.n, (0, 0))]
            heapq.heapify(queue)
            goal = (self.n - 1, self.n - 1)
            while (queue):
                curr = heapq.heappop(queue)
                if curr[1] == goal:
                    return self.adjacency_map.get(curr[1])[0]

                children = self.get_child(curr[1])
                for child in children:
                    if child not in self.adjacency_map or self.adjacency_map.get(curr[1])[0] + 1 < \
                            self.adjacency_map.get(child)[0]:
                        self.adjacency_map[child] = [self.adjacency_map.get(curr[1])[0] + 1, child]
                        heapq.heappush(
                            queue, (self.adjacency_map.get(child)[0] + self.get_h_val(child), child)
                        )

        return -1


if __name__ == '__main__':
    test_case = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0]
    ]
    dist = Solution().shortestPathBinaryMatrix(test_case)
    print(dist)