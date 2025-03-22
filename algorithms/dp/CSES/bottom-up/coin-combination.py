import sys
MOD = 10**9 + 7

n, target = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))

dp = [0] * (target + 1)
dp[0] = 1
MOD = 10**9+7
coins.sort()
for amount in range(1, target + 1):
    for coin in coins:
        remaining = amount - coin
        if remaining < 0:
            break
        dp[amount] = (dp[amount] + dp[remaining]) % MOD
print(dp[target])
