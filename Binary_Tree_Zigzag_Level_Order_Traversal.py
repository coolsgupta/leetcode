# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def level_trav(lv_dt, node, level):
            if not node:
                return

            if level not in lv_dt:
                lv_dt[level] = []
            lv_dt[level].append(node.val)
            level_trav(lv_dt, node.left, level + 1)
            level_trav(lv_dt, node.right, level + 1)

        lv_dt = {}
        level_trav(lv_dt, root, 1)

        for level in lv_dt:
            if level % 2 == 0:
                lv_dt[level].reverse()

        return lv_dt.values()