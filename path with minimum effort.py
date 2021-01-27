import heapq

class Solution:
    def get_child(self, point, actions, heights):
        children = []
        for action in actions:
            children.append(tuple(map(lambda i, j: i + j, point, action)))

        return children

    def minimumEffortPath(self, heights):
        visited = {(0, 0)}
        queue = [(0, heights[0][0], 0, 0)]
        heapq.heapify(queue)
        actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(heights), len(heights[0])
        goal = (n - 1, m - 1)
        adjacency_map = {
            (0, 0): ((-1, -1), 0)
        }

        while queue:
            current = heapq.heappop(queue)
            current_point = (current[2], current[3])
            if current_point == goal:
                break

            reachable_points = self.get_child(current_point, actions, heights)

            for point in reachable_points:
                if 0 <= point[0] < n and 0 <= point[1] < m:
                    point_height = heights[point[0]][point[1]]
                    height_diff = abs(point_height - current[1])

                    if point not in visited or height_diff < adjacency_map[point][1] and adjacency_map[current_point][0] != point:
                        print(point)
                        visited.add(point)
                        adjacency_map[point] = ((current_point[0], current_point[1]), height_diff)

                        heapq.heappush(queue, (height_diff, point_height, point[0], point[1]))

        print(adjacency_map)
        current = goal
        stack = []
        max_h = 0
        while current != (0, 0):
            stack.append(heights[current[0]][current[1]])
            current = adjacency_map[current][0]
            max_h = max(max_h, adjacency_map[current][1])

        stack.append(heights[0][0])
        print(stack[::-1])
        return max_h

if __name__ == '__main__':
    case = [[1,10,6,7,9,10,4,9]]
    ans = Solution().minimumEffortPath(case)
    print(ans)
