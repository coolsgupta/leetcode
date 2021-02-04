class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        rem = [0] * 60
        res = 0
        for x in time:
            c_rem = x % 60
            if (c_rem == 0):
                res += rem[0]
            else:
                res += rem[60 - c_rem]

            rem[c_rem] += 1

        return res