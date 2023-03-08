def uniquePaths(m, n):
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i != 0 or j != 0:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(1, 2))
