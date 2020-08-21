"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            child_vals = [root.val]
            if root.children:
                for child in root.children:
                    child_vals.extend(self.preorder(child))
            return child_vals
        else:
            return []

