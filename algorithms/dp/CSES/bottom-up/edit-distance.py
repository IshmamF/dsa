str1 = input()
str2 = input()

m, n = len(str1), len(str2)
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == n:
            dp[i][j] = abs(m - j)
        if j == m:
            dp[i][j] = abs(n - i)
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if str1[j] != str2[i]:
            dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        else:
            dp[i][j] = dp[i+1][j+1]
print(dp[0][0])