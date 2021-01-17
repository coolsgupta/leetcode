# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        else:
            paths = []

            if root.left:
                paths.extend(self.binaryTreePaths(root.left))

            if root.right:
                paths.extend(self.binaryTreePaths(root.right))

            return [str(root.val) + '->' + x for x in paths]