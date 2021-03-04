import collections


class Solution:
    def slidingPuzzle(self, puzzle):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def getChild(state):
            state = list(state)
            index = state.index(0)
            curr_row, curr_col = index // m, index % m
            child = []
            possible_child = [[curr_row + 1, curr_col], [curr_row - 1, curr_col], [curr_row, curr_col + 1], [curr_row, curr_col - 1]]
            for x, y in possible_child:
                if 0 <= x < n and 0 <= y < m:
                    node = state.copy()
                    node[index], node[x * m + y] = node[x * m + y], node[index]
                    node = tuple(node)
                    if node not in visited:
                        visited.add(node)
                        child.append(node)

            return child

        start = []
        n, m = len(puzzle), len(puzzle[0])
        goal = tuple([x for x in range(n*m)])
        for row in puzzle:
            start += row

        start = tuple(start)
        queue = collections.deque([(start, 0)])
        visited = {start}
        while queue:
            state, dist = queue.pop()
            if state == goal:
                return dist

            for child in getChild(state):
                queue.appendleft((child, dist + 1))

        return -1


if __name__ == '__main__':
    board = [[5,1,2],[8,7,6],[4,3,0]]
    res = Solution().slidingPuzzle(board)
    print(res)
