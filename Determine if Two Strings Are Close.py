class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)

        if a.keys() == b.keys() and Counter(a.values()) == Counter(b.values()):
            return True

        return False