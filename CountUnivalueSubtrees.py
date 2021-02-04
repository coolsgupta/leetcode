# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, node):
        if not node:
            return True

        flag = True
        if node.left:
            flag = self.check(node.left) and flag and node.val == node.left.val

        if node.right:
            flag = self.check(node.right) and flag and node.val == node.right.val

        if flag:
            self.count += 1

        return flag

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.check(root)
        return self.count
