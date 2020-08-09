class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # items = set()
        # for num in nums:
        #     if num not in items:
        #         items.add(num)
        #     else:
        #         items.remove(num)
        # return items.pop()

        a = 0
        for num in nums:
            a ^= num
        return a
