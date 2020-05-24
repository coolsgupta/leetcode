class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True
        # m = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        for i in range(len(coordinates)-2):
            y21 = (coordinates[i + 1][1] - coordinates[i][1])
            x21 = (coordinates[i + 1][0] - coordinates[i][0])
            y32 = (coordinates[i + 2][1] - coordinates[i + 1][1])
            x32 = (coordinates[i + 2][0] - coordinates[i + 1][0])

            # if (coordinates[i + 1][1] - coordinates[i][1])* == *(coordinates[i + 3][1] - coordinates[i + 2][1]):
            if y21*x32 != y32*x21:
                return False
            # y = (coordinates[i + 1][1] - coordinates[i][1])
            # x = (coordinates[i + 1][0] - coordinates[i][0])
            # mp = y/x
            # if mp != m:
            #     return False
        return True

Solution().checkStraightLine([[1,2],[2,3],[3,5]])