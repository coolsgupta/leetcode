class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while (X < Y):
            if Y % 2 == 1:
                Y += 1
            else:
                Y /= 2

            count += 1

        return count + X - Y

if __name__ == '__main__':
    ans = Solution().brokenCalc(1, 100)
    print(ans)

1,2,4,8,7,6,5,10,20,40,80