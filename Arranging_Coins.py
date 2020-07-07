
def arrangeCoins_1(self, n):
    """
    :type n: int
    :rtype: int
    """
    i = 0
    c = 0
    while(c<=n):
        i += 1
        c += i
    return i-1


def arrangeCoins_2(self, n):
    """
    :type n: int
    :rtype: int
    """

    return (2*n + 0.25)**0.5 - 0.5


def arrangeCoins_3(self, n):
    """
    :type n: int
    :rtype: int
    """
    beg, end = 0, n

    while beg <= end:
        x = (beg + end) // 2
        curr_sum = x * (x + 1) // 2
        if curr_sum == n:
            return x
        if n < curr_sum:
            end = x - 1
        else:
            beg = x + 1
    return end