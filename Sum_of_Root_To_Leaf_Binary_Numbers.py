# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def sum_tree(root, num):
            if root:
                if not root.left and not root.right:
                    return int(num + str(root.val), 2)
                else:
                    return sum_tree(root.left, num + str(root.val)) + sum_tree(root.right, num + str(root.val))

            else:
                return 0

        return sum_tree(root, '')

