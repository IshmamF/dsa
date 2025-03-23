import sys
n, target = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))

INF = 1000000000
dp = [INF] * (target + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, target + 1):    
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[target]) if dp[target] != INF else print(-1)
