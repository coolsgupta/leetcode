class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        for x in d:
            i = 0
            for ch in s:
                if ch == x[i]:
                    i += 1
                    if i == len(x):
                        return x

        return ''
