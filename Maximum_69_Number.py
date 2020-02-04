class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        p = 1
        num = 0
        cnum = 0
        nnum = num
        while num:
            n = num%10
            if n==6:
                nnum = cnum + 9*p
            else:
                nnum += n*p
            cnum += n*p
            num = num/10
            p *= 10
        return nnum