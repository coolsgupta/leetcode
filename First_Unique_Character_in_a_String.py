#First Unique Character in a String
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
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

        d = get_dict(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        else:
            return -1


