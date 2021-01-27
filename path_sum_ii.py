# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum_path: int) -> List[List[int]]:
        if not root:
            return []

        def paths(current_paths, root):
            if not root:
                return current_paths

            new_paths = [x + [root.val] for x in current_paths if sum(x) + root.val <= sum_path]

            left_paths = paths(new_paths, root.left)
            right_paths = paths(new_paths, root.right)
            return left_paths + right_paths

        all_paths = paths([[root.val]], root.left)
        all_paths.extend(paths([[root.val]], root.right))

        return [x for x in all_paths if sum(x) == sum_path]