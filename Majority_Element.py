class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_dict(x):
            d = {}
            for y in x:
                if y not in d:
                    d[y] = 1
                else:
                    d[y] += 1
            return d

        d = get_dict(nums)
        max = 0
        for k in d:
            if d[k] > max:
                max = d[k]
                km = k
        return km
