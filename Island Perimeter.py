class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(grid[0])
        perimeter = 0
        i = -1
        j = -1
        i0 = -1
        j0 = -1
        for row in grid:
            try:
                ni = row.index(1)
                nj = len_row - row[::-1].index(1) - 1

                try:
                    ni0 = row[ni:nj + 1].index(0)
                    nj0 = len_row - row[ni:nj + 1][::-1].index(0) - 1

                    if i0 == -1:
                        perimeter += nj0 - ni0 + 3
                        i0 = ni0
                        j0 = nj0

                    else:
                        perimeter += 2

                    i0 = ni0
                    j0 = nj0

                except:
                    pass

                if i == -1:
                    perimeter += nj - ni + 3
                    i = ni
                    j = nj

                else:
                    perimeter += abs(i - ni) + abs(j - nj) + 2

                i = ni
                j = nj

            except:
                perimeter += 0
                if perimeter > 0:
                    break

        perimeter += abs(j - i) + 1

        if i0 != -1:
            perimeter -= j0 - i0 + 1

        return perimeter


if __name__ == '__main__':
    Solution().islandPerimeter([[1,1,1],[1,0,1],[1,0,1]])