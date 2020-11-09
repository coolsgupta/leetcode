# def traverse(self, traversal_map, node, col):
    # if not node:
    #     return traversal_map
    #
    # if col not in traversal_map:
    #     traversal_map[col] = []
    #
    # traversal_map[col].append(node.val)
    # traversal_map = self.traverse(traversal_map, node.left, col - 1)
    # traversal_map = self.traverse(traversal_map, node.right, col + 1)
    #
    # return traversal_map


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = [(0, 0, root)]
        traversal_map = {}
        # traversal_list = []
        while (queue):
        #     current = queue.pop(0)
        #     traversal_list.append(current)
        #     queue.append((current[0] - 1, current[1] + 1, current[2].left))
        #     queue.append((current[0] + 1, current[1] + 1, current[2].right))
            current = queue.pop(0)
            if not current[2]:
                continue

            if current[0] not in traversal_map:
                traversal_map[current[0]] = []

            traversal_map[current[0]].append((current[1], current[2].val))
            queue.append((current[0] - 1, current[1] + 1, current[2].left))
            queue.append((current[0] + 1, current[1] + 1, current[2].right))

        print(traversal_map)

        return list(map(lambda x: x[1], sorted({col: list(map(lambda x: x[1], sorted(traversal_map[col]))) for col in traversal_map}.items())))
