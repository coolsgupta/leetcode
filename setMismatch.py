class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        new_sum = sum(nums);
        less_sum = sum(set(nums))
        req_sum = len(nums) * (len(nums) + 1) // 2
        return [new_sum - less_sum, req_sum - less_sum]
