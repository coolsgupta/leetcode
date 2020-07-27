class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dt = {}
        res = []
        for num in nums:
            if num not in dt:
                dt[num] = None
            else:
                dt.pop(num)
        return list(dt.keys())