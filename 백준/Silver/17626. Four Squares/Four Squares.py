n = int(input())
dp = [4] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    start = 1
    #min_val = 4
    while start ** 2 <= i:
        dp[i] = min(dp[i], dp[i-start**2])
        start += 1
    dp[i] += 1
print(dp[-1])
        

