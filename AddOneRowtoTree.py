# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            temp = TreeNode(val, root)
            return temp

        queue = deque()
        queue.append((1, root))
        while (queue):
            curr = queue.popleft()
            if curr[0] < depth - 1:
                if curr[1].left:
                    queue.append((curr[0] + 1, curr[1].left))

                if curr[1].right:
                    queue.append((curr[0] + 1, curr[1].right))

            elif curr[0] == depth - 1:
                curr[1].left = TreeNode(val, curr[1].left)
                curr[1].right = TreeNode(val, None, curr[1].right)

        return root
