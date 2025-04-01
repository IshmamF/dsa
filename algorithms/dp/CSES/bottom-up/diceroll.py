n = int(input())

dp = [0] * (n + 1)
dp[0] = 1 

for count in range(1, n+1):
    for roll in range(1, 7):
        if roll > count:
            break
        dp[count] = (dp[count] + dp[count - roll]) % (1e9+7)

print(int(dp[n]))