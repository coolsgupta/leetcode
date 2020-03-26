class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if i else 1 for i in row[::-1]] for row in A]

    def flipAndInvertImage_alternate(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 - x for x in row[::-1]] for row in A]
