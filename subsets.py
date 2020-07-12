class Solution:
    def subsets(self, nums):
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        subsets = []
        for i in range(2**n, 2**(n+1)):
            bit_map = bin(i)[3:]
            subsets.append([nums[i] for i in range(n) if bit_map[i]=='1'])
        return subsets

Solution2().subsets([1,2,3])