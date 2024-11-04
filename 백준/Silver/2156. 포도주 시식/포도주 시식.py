import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    dp[2] = arr[0] + arr[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i-3] + arr[i-2] + arr[i-1], dp[i-1], dp[i-2] + arr[i-1])
    print(dp[-1])