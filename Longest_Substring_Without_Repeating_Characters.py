class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        win = []
        maxl = 0
        for c in s:
            if c not in win:
                win.append(c)
            else:
                maxl = max(maxl, len(win))
                for x in win:
                    win.pop(0)
                    if c not in win:
                        win.append(c)
                        break

        return max(maxl, len(win))

s = "yfsrsrpzuya"
print (Solution().lengthOfLongestSubstring(s))