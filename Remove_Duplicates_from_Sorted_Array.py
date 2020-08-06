class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        move_index = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                move_index += 1
            else:
                nums[i - move_index] = nums[i]

        return len(nums)
