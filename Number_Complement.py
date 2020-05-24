class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        comp = 0
        while num:
            r = num % 2
            x = 0 if r else 1
            comp += x * (2 ** i)
            num = num // 2
            i += 1
        return comp
        # return int(''.join(['0' if int(x) else '1' for x in '{0:b}'.format(num)]), 2)
