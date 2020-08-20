# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        def find_min_k(root):
            if not root or len(stack) >= k:
                return

            find_min_k(root.left)
            stack.append(root.val)
            find_min_k(root.right)

        find_min_k(root)
        return stack[k - 1]
