class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = []

        def backtrack(first=0):
            if first == len_nums:
                res.append(nums[:])

            for i in range(first, len_nums):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        backtrack()
        return res

