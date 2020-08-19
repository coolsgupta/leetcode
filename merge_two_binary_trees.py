from create_binary_tree_from_list import create_tree, print_tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2

        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

if __name__ == '__main__':
    t1 = create_tree([1,3,2,5])
    t2 = create_tree([2,1,3, None,4, None,7])
    print_tree(t1)
    print('**********')
    print_tree(t2)
    Solution().mergeTrees(t1, t2)
    print('**********')
    print_tree(t1)