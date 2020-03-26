class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        m = len(matrix)
        ln = []
        for i in range(m):
            x = min(matrix[i])
            if x == max(t_matrix[matrix[i].index(x)]):
                ln.append(x)
        return ln

ans = Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
print(ans)