# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        level_dict = {}

        def level_trav(root, level):
            if level not in level_dict:
                level_dict[level] = []
            if root:
                level_dict[level].append(root.val)
                level_trav(root.left, level + 1)
                level_trav(root.right, level + 1)
            else:
                level_dict[level].append(None)

        level_trav(root, 0)
        for level in level_dict:
            n = len(level_dict[level])
            if level_dict[level] != level_dict[level][::-1]:
                return False

        return True

