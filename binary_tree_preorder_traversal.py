# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        curr = root
        vals = []

        while True:
            if curr:
                vals.append(curr.val)
                stack.append(curr)
                curr = curr.left

            elif (stack):
                curr = stack.pop()
                curr = curr.right

            else:
                break

        return vals


