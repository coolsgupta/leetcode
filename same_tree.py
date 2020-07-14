# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check_tree(r1, r2):
            if not r1 and not r2:
                return True

            elif not r1 or not r2:
                return False

            return r1.val == r2.val and check_tree(r1.left, r2.left) and check_tree(r1.right, r2.right)

        return check_tree(p, q)




