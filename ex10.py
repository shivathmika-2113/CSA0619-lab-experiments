
def binomial(n, k):
    dp = [[0 for j in range(k+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][k]


n = 5
k = 2

print("Binomial Coefficient:", binomial(n, k))
