# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp1 = None
        temp2 = head

        while temp2:
            temp3 = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3

        return temp1