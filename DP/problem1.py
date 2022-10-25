def add_numbers(n):
    dp = [None]*(n+1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp[-1]
