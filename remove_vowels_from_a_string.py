class Solution:
    def removeVowels(self, S: str) -> str:
        # new_s = ''
        # for ch in S:
        #     if ch in ('a', 'e', 'i', 'o', 'u'):
        #         continue
        #     new_s = new_s + ch
        #
        # return new_s
        return ''.join([s for s in S if s not in {'a', 'e', 'i', 'o', 'u'}])