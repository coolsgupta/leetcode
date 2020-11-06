# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i, j = l1, l2

        res = ListNode()
        temp = res

        while i and j:
            if i.val <= j.val:
                temp.next = i
                i = i.next

            else:
                temp.next = j
                j = j.next

            temp = temp.next

        temp.next = i if i is not None else j

        return res.next
