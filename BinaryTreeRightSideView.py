class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels_map = []
        queue = [(0, root)]
        while (queue):
            curr = queue.pop(0)
            if not curr[1]:
                continue

            if curr[0] >= len(levels_map):
                levels_map.append([])

            levels_map[curr[0]].append(curr[1].val)
            queue.append((curr[0] + 1, curr[1].left))
            queue.append((curr[0] + 1, curr[1].right))

        res = []
        for level in levels_map:
            res.append(level[-1])

        return res