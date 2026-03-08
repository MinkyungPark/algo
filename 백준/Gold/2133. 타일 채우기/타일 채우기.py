N = int(input())


def sol(n):
    if n % 2 != 0:
        return 0
    
    dp = [0] * (N + 1)
    dp[2] = 3
    
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(2, i - 2, 2):
            dp[i] += dp[j] * 2
    
    return dp[n]

print(sol(N))