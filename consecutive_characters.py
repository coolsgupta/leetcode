class Solution:
    def maxPower(self, s: str) -> int:
        max_c = 0
        c = 0
        curr = s[0]
        for ch in s:
            if ch == curr:
                c += 1

            else:
                max_c = max(c, max_c)
                c = 1
                curr = ch

        max_c = max(c, max_c)

        return max_c


s = "leetcode"
res = Solution().maxPower(s)
print(s)
