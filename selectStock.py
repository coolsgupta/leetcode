def selectStock(saving, currentValue, futureValue):
    dp = [[0]*(saving+1) for _ in range(len(currentValue) + 1)]

    for i in range(1, len(currentValue) + 1):
        for j in range(1, saving + 1):
            if currentValue[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], futureValue[i-1] - currentValue[i - 1] + dp[i-1][j - currentValue[i-1]])

            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(currentValue)][saving]


if __name__ == '__main__':
    res = selectStock(
        500,
        [150,199,200,168,153],
        [140,175,199,121,111]
    )
    print(res)



