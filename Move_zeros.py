class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1

        for i in range(n, len_nums):
            nums[i] = 0
