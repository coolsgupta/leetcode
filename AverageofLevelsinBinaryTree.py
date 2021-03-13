# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels_map = {}

        queue = deque()
        queue.append((0, root))
        while (queue):
            curr = queue.popleft()
            if not curr:
                continue

            if curr[0] not in levels_map:
                levels_map[curr[0]] = [0, 0]

            levels_map[curr[0]][0] += curr[1].val
            levels_map[curr[0]][1] += 1
            if curr[1].left:
                queue.append((curr[0] + 1, curr[1].left))

            if curr[1].right:
                queue.append((curr[0] + 1, curr[1].right))

        return list(map(lambda x: x[0] / x[1], levels_map.values()))

