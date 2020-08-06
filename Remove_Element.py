class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        move_index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                move_index += 1
            else:
                nums[i - move_index] = nums[i]
        if move_index:
            nums = nums[:-move_index]
        return len(nums)
