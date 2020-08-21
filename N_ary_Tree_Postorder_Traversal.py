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
            if root.children:
                return [x for y in [self.postorder(x) for x in root.children] for x in y].append(root.val)
            else:
                return [root.val]
        return []

