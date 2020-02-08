#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         sum = None
#         carry = 0
#         while (l1 and l2):
#             s = l1.val + l2.val + carry
#             ptr = ListNode(s % 10)
#             carry = s / 10
#             if not sum:
#                 sum = ptr
#             l1 = l1.next
#             l2 = l2.next
#             if (l1 or l2):
#                 ptr.next = ListNode()
#                 ptr = ptr.next
#         if l1:
#             ptr.val = l1.val
#             l1 = l1.next
#             if l1:
#                 ptr.next = ListNode()
#                 ptr = ptr.next
#         if l2:
#             ptr.val = l2.val
#             l2 = l2.next
#             if l2:
#                 ptr.next = ListNode()
#                 ptr = ptr.next
#         return sum
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_sum = None
        ptr = None
        carry = 0
        lptr = None
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = int(s / 10)
            d = s % 10

            ptr = ListNode(d)
            if not list_sum:
                list_sum = lptr = ptr
            else:
                lptr.next = ptr
                lptr = lptr.next

            l1 = l1.next
            l2 = l2.next

        ptr = l1 if l1 else l2

        if ptr and carry:
            while ptr and carry:
                ptr.val += carry
                carry = int(ptr.val / 10)
                ptr.val = ptr.val % 10
                lptr.next = ptr
                lptr = lptr.next
                ptr = ptr.next
        if carry:
            lptr.next = ListNode(carry)
            lptr = lptr.next

        if ptr:
            if not list_sum:
                list_sum = ptr
            else:
                lptr.next = ptr

        return list_sum


num1 = 99
num2 = 1


def num_to_list(num):
    ls = None
    ptr = None
    while num:
        d = num%10
        num = int(num/10)
        if ptr:
            ptr.next = ListNode(d)
            ptr = ptr.next
        else:
            ls = ptr = ListNode(d)
    return ls


num1 = num_to_list(num1)
num2 = num_to_list(num2)

list_sum = Solution().addTwoNumbers(num1,num2)
while list_sum:
    print(list_sum.val)
    list_sum = list_sum.next