
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = None
        carry = 0
        while (l1 and l2):
            s = l1.val + l2.val + carry
            ptr = ListNode(s % 10)
            carry = s / 10
            if not sum:
                sum = ptr
            l1 = l1.next
            l2 = l2.next
            if (l1 or l2):
                ptr.next = ListNode()
                ptr = ptr.next
        if l1:
            ptr.val = l1.val
            l1 = l1.next
            if l1:
                ptr.next = ListNode()
                ptr = ptr.next
        if l2:
            ptr.val = l2.val
            l2 = l2.next
            if l2:
                ptr.next = ListNode()
                ptr = ptr.next
        return sum

