class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num and not (num & (num - 1))):
            c = 0
            while num > 1:
                num >>= 1
                c += 1

            if c % 2 == 0:
                return True

        return False
