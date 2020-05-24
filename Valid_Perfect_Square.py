from copy import deepcopy
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        cnum = deepcopy(num)
        while cnum>0:
            sqrt = cnum//2
            sqrt_sq = sqrt**2
            if sqrt_sq == num:
                return True
            if sqrt_sq < num:
                beg, end = sqrt, sqrt*2 + 1
                while beg <= end:
                    mid = (beg + end)//2
                    mid_sq = mid**2
                    if mid_sq == num:
                        return True
                    elif mid_sq > num:
                        end = mid - 1
                    else:
                        beg = mid + 1
            cnum = cnum//2
        return False

Solution().isPerfectSquare(100)