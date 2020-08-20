# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        elif not root.left and not root.right:
            return 1

        elif not root.left:
            return 1 + self.minDepth(root.right)

        elif not root.right:
            return 1 + self.minDepth(root.left)

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
