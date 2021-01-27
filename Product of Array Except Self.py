class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        left_p = [1] * len(nums)
        right_p = [1] * len(nums)
        len_nums = len(nums)

        for i in range(1, len_nums):
            left = left * nums[i - 1]
            left_p[i] = left

            right = right * nums[len_nums - i]
            right_p[len_nums - i - 1] = right

        for i in range(len_nums):
            nums[i] = left_p[i] * right_p[i]

        return nums