# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        item_dict = {}

        def iterate(node, parent=None, level=0):
            if node:
                item_dict[node.val] = (level, parent)
                iterate(node.left, node, level + 1)
                iterate(node.right, node, level + 1)
            return

        iterate(root)

        if x in item_dict and y in item_dict:
            xd = item_dict[x]
            yd = item_dict[y]
            if xd[0] == yd[0] and xd[1] != yd[1]:
                return True
        return False
