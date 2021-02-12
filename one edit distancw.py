class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False

        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                temp = s[:i] + t[i] + s[i + 1:]
                if temp == t:
                    return True

                temp = s[:i] + s[i + 1:]
                if temp == t:
                    return True

                temp = s[:i] + t[i] + s[i:]
                if temp == t:
                    return True

                break

        if s[:-1] == t or t[:-1] == s:
            return True

        return False