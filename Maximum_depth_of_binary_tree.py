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

        def depth(node, level, max_level):
            if not node:
                return max_level

            if level > max_level:
                max_level = level

            max_level = max(depth(node.left, level + 1, max_level), depth(node.right, level + 1, max_level))
            return max_level

        return depth(root, 1, 0)