from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = []

        def dfs(perm, nums_count_map):
            if len(perm) == len_nums:
                res.append(perm[:])

            for n in nums_count_map:
                if nums_count_map[n] > 0:
                    perm.append(n)
                    nums_count_map[n] -= 1
                    dfs(perm, nums_count_map)
                    perm.pop()
                    nums_count_map[n] += 1

        dfs([], Counter(nums))
        return res
