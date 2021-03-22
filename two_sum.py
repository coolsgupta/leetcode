class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashed_complements = {}
        for i, x in enumerate(nums):
            comp = target - x
            if comp in hashed_complements:
                return [hashed_complements[comp], i]

            hashed_complements[x] = i

        return []

if __name__ == '__main__':
    case = [1,1,2,2,3,3]
    print(Solution.twoSum(case, 1))