class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""

        for i in range(n):
            res += word1[i] + word2[i]

        res += max(word1, word2, key=lambda x: len(x))[n:]

        return res
