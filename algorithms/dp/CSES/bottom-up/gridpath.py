n = int(input())
grid = []

for _ in range(n):
    row = input()
    grid.append(list(row))

MOD = 10**9 + 7


dp = [[0] * (n) for _ in range(n)]
if grid[n-1][n-1] == '*':
    print(0)
else:
    dp[n-1][n-1] = 1
    for i in range(n-2, -1, -1):
        if grid[n-1][i] == '*':
            break
        dp[n-1][i] = 1
    for j in range(n-2, -1, -1):
        if grid[j][n-1] == '*':
            break
        dp[j][n-1] = 1 

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if grid[i][j] != '*':
                dp[i][j] = (dp[i+1][j] + dp[i][j+1]) % MOD
    print(dp[0][0])