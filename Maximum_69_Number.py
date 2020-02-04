class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        p = 1
        fp = 0
        nnum = num
        while num:
            n = num % 10
            if n == 6:
                fp = p
            num = num/10
            p = p*10
        return nnum + 3*fp


obj = Solution()
n = obj.maximum69Number(9999)
print(n)