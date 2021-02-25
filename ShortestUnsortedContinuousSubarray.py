class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        count = 0
        flagi = True
        flagj = True
        i = 0
        j = len(nums) - 1
        while (i < j):
            if nums[i] == sorted_nums[i] and flagi:
                i += 1

            else:
                flagi = False

            if nums[j] == sorted_nums[j] and flagj:
                j -= 1

            else:
                flagj = False

            if not (flagi or flagj):
                return j - i + 1

        return 0

