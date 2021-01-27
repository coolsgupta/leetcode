# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, mini, maxi):
            if not root:
                return True

            if root.val > maxi or root.val < mini:
                return False

            return valid(root.left, mini, root.val - 1) and valid(root.right, root.val + 1, maxi)

        return valid(root, float('-inf'), float('inf'))
