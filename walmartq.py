def numCoinsRequired(coins, amount):
    coins.sort()

    dp = [amount+1] * (amount + 1)
    dp[0] = 0
    for coinDem in coins:
        for val in range(coinDem, amount+1):
            dp[val] = min(dp[val], dp[val - coinDem] + 1)

    print(dp)
    return -1 if dp[amount] > amount else dp[amount]


if __name__ == '__main__':
    coinsAvailable = [2, 5]
    amount = 11
    res = numCoinsRequired(coinsAvailable, amount)
    print(res)
