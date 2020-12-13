def longestSubsequence(x, y):
    # Write your code here
    len_x = len(x)
    len_y = len(y)
    opt = [[0 for i in range(max(len_y, len_x) * 2)]
          for i in range(max(len_y, len_x) * 2)]

    for i in range(1, len_y + 1):
        for j in range(1, len_x + 1):
            if (x[j - 1] == y[i - 1]):
                opt[i][j] = 1 + opt[i - 1][j - 1]

            else:
                opt[i][j] = opt[i][j - 1]

    ans = 0
    for i in range(1, len_y + 1):
        ans = max(ans, opt[i][len_x])

    return ans
