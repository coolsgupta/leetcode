class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            res.append(list(map(lambda x: x ^ 1, row))[::-1])

        return res