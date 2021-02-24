class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for x in nums:
            temp = curr
            curr = max(prev + x, curr)
            prev = temp

        return curr


