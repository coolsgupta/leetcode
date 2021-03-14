class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all_strings = set()
        for i in range(len(s) - k + 1):
            all_strings.add(s[i: i + k])

        return len(all_strings) == 1 << k
