# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversalRecursive(self, root):
        if not root:
            return []

        vals = []
        if root.left:
            vals = self.inorderTraversalRecursive(root.left)

        vals.append(root.val)

        if root.right:
            vals = vals + self.inorderTraversalRecursive(root.right)

        return vals

    def inorderTraversalIterative(self, root):
        if not root:
            return []

        stack = [root]
        vals = []
        curr = root.left

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()
                vals.append(curr.val)
                curr = curr.right

            else:
                break

        return vals

