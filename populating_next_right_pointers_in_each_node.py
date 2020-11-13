"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [(0, root)]
        while (queue):
            current = queue.pop(0)
            if queue and queue[0][0] == current[0]:
                current[1].next = queue[0][1]

            else:
                current[1].next = None

            if current[1].left:
                queue.append((current[0] + 1, current[1].left))

            if current[1].right:
                queue.append((current[0] + 1, current[1].right))

        return root


