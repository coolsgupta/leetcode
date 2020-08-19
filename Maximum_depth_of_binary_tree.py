# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        level = 1

        def depth(root, level):
            if not root:
                return level - 1

            return max([level, depth(root.left, level + 1), depth(root.right, level + 1)])

        return max([level, depth(root.left, level + 1), depth(root.right, level + 1)])
