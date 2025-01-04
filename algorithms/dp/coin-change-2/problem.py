# Top Down Memoized Solution
def change(amount, coins):
    memo = {}

    def dfs(i, current):

        if i == len(coins):
            return 1 if current == amount else 0
        if current > amount:
            return 0
        if (i, current) in memo:
            return memo[(i, current)]

        skip = dfs(i + 1, current)
        include = dfs(i, current + coins[i])
        memo[(i, current)] = skip + include
        return skip + include

    return dfs(0, 0)

# Bottom Up Approach
def change(amount, coins):
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    
    '''
    for k in range(amount + 1):
        if (k >= coins[0] and k % coins[0] == 0) or k == 0:
            dp[0][k] = 1
    '''

    for i in range(len(coins), -1, -1):
        for j in range(amount, -1, -1):
            if i == len(coins):
                continue
            skip = dp[i + 1][j]
            include = 0
            if j + coins[i] <= amount:
                include = dp[i][j + coins[i]]
            dp[i][j] = skip + include
    print(dp)

    return dp[0][0]

print(change(5, [1,2,5]))