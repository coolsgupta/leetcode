# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.stack.append(node)
        self.inorder(node.right)

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.stack = []
        current_sum = 0
        self.inorder(root)
        while (self.stack):
            curr = self.stack.pop()
            current_sum += curr.val
            curr.val = current_sum

        return root