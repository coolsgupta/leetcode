class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ea = []
        oa = []
        for n in A:
            if n & 1:
                oa.append(n)
            else:
                ea.append(n)
        ea.extend(oa)
        return ea