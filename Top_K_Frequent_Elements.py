class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dt = {}
        for e in nums:
            if e not in dt:
                dt[e] = 0
            dt[e] += 1
        ls = sorted(dt.items(), key=lambda x: -x[1])
        return [x[0] for x in ls[:k]]
