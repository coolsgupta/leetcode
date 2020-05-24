class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = dict.fromkeys(J)
        c = 0
        for x in S:
            if x in J:
                c += 1
        return c