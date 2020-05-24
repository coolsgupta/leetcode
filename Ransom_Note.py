class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        def get_dict(x):
            d = {}
            for y in x:
                if y not in d:
                    d[y] = 0
                else:
                    d[y] += 1
            return d

        r = get_dict(ransomNote)
        m = get_dict(magazine)
        for k in r:
            if k not in m or r[k] > m[k]:
                return False
        return True