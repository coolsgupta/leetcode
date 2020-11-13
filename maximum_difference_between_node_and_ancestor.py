# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def max_tree_diff(node, min_anc, max_anc):
            if not node:
                return abs(max_anc - min_anc)

            max_anc = max(max_anc, node.val)
            min_anc = min(min_anc, node.val)

            diff_left = max_tree_diff(node.left, min_anc, max_anc)
            diff_right = max_tree_diff(node.right, min_anc, max_anc)

            return max(diff_left, diff_right)

        return max_tree_diff(root, root.val, root.val)
