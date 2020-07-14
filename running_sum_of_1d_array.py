class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
        return sums