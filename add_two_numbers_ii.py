# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def create_linked_list_from_list(self, ls):
        head = ListNode()
        head.val = ls[0]
        if len(ls) == 1:
            return head
        head.next = self.create_linked_list_from_list(ls[1:])
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        while (l1):
            num1 *= 10
            num1 += l1.val
            l1 = l1.next

        while (l2):
            num2 *= 10
            num2 += l2.val
            l2 = l2.next

        res = num1 + num2

        return self.create_linked_list_from_list(str(res))