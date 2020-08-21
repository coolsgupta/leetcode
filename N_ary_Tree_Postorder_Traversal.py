"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            child_vals = []
            if root.children:
                for child in root.children:
                    child_vals.extend(self.postorder(child))
            child_vals.append(root.val)
            return child_vals
        else:
            return []
    