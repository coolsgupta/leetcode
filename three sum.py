class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        triplets = {}
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                nums_dict = nums
                pair = -(nums[x] + nums[y])
                if pair in nums_dict:
                    trip = tuple(sorted([nums[x], nums[y], pair]))
                    if trip not in triplets:
                        triplets[trip] = 0
        return list(triplets.keys())


class SolutionHashed(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        triplets = set()
        targets = {}
        for k, target in enumerate(nums[:-2]):
            if target not in targets:
                targets[target] = None

                hashed_complements = {}
                for x in nums[k + 1:]:
                    comp = -(target + x)

                    if comp in hashed_complements:
                        triplets.add(tuple(sorted([target, comp, x])))

                    hashed_complements[x] = None

        return list(triplets)
