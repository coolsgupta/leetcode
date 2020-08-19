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

        def sum_tree(n1, n2, p, child=''):
            if n1 and n2 and n1.val and n2.val:
                n1.val += n2.val
                sum_tree(n1.left, n2.left, n1, 'left')
                sum_tree(n1.right, n2.right, n1, 'right')

            elif not (n1 or n2):
                return

            else:
                new_node = None

                if not n1:
                    new_node = n2

                elif not n2:
                    new_node = n1

                if child == 'left':
                    p.left = new_node

                elif child == 'right':
                    p.right = new_node

                if not n1:
                    sum_tree(None, n2.left, n1, 'left')
                    sum_tree(None, n2.right, n1, 'right')

                else:
                    sum_tree(n1.left, None, n1, 'left')
                    sum_tree(n1.right, None, n1, 'right')

        sum_tree(t1, t2, None)
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