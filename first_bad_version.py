def isBadVersion(m):
    if m == ver:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg, end = 0, n-1
        while (beg <= end):
            if beg == end:
                return beg + 1

            mid = int((beg + end) / 2)
            if isBadVersion(mid + 1):
                if not isBadVersion(mid):
                    return mid + 1

                else:
                    end = mid - 1

            else:
                beg = mid + 1

while(1):
    ver = int(input('ver : '))
    n = int(input('n : '))
    print(Solution().firstBadVersion(n))