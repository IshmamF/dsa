# Top down memoized solution, however we make two decisions
def coinChange(coins, amount):
    
    memo = {}
    def dfs(i, amount):

        if i == len(coins):
            return 0 if amount == 0 else float('inf')
        if (i, amount) in memo:
            return memo[(i, amount)]

        minimum = dfs(i + 1, amount)

        newAmount = amount - coins[i]
        if newAmount >= 0:
            include = 1 + dfs(i, newAmount)
            minimum = min(minimum, include) 
        memo[(i, amount)] = minimum
        return minimum 
    
    minimumCoins = dfs(0, amount) 
    return minimumCoins if minimumCoins != float('inf') else -1

def testFunc(func):
    coins = [1, 2, 5]
    amount = 11
    print(func(coins, amount))
    coins = [2]
    amount = 3
    print(func(coins, amount))
    coins = [1]
    amount = 0
    print(func(coins, amount))

testFunc(coinChange)

# Top down memoized solution, however we try every possible coin
def coinChange(coins, amount):
    memo = {}
    def dfs(amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        if amount in memo:
            return memo[amount]
        minimum = float('inf')
        for n in coins:
            value = 1 + dfs(amount - n)
            minimum = min(minimum, value)
        memo[amount] = minimum
        return minimum
    
    minimumCoins = dfs(amount)
    return minimumCoins if minimumCoins != float('inf') else -1

testFunc(coinChange)

# Hashset Approach
def coinChange(coins, amount):

    amountLeft = set()
    amountLeft.add((amount, 0))
    possibleMinimums = -1
    visited = {}
    

    while amountLeft:
        amt, cnt = amountLeft.pop()

        if amt in visited and cnt >= visited[amt]:
           continue
        visited[amt] = cnt

        if amt == 0:
            if possibleMinimums == -1:
                possibleMinimums = cnt
            else:
                possibleMinimums = min(possibleMinimums,cnt)

        for n in coins:
            diff = amt -  n
            if diff > 0:
                if diff in visited:
                    if cnt + 1 < visited[diff]:
                        amountLeft.add((diff, cnt + 1))
                else:
                    amountLeft.add((diff, cnt + 1))
            elif diff == 0:
                if possibleMinimums == -1:
                    possibleMinimums = cnt + 1
                else:
                    possibleMinimums = min(possibleMinimums,cnt + 1)
    return possibleMinimums

testFunc(coinChange)

# Bottom Up Approach

def coinChange(coins, amount):

    dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 0

    for k in range(1, amount + 1):
        firstCoin = coins[0]
        if k >= firstCoin and dp[0][k-firstCoin] != -1:
            dp[0][k] = 1 + dp[0][k-firstCoin]

    for i in range(1, len(coins) + 1):
        currentCoin = coins[i-1]
        for j in range(amount + 1):
            if j == 0:
                dp[i][j] = 0
                continue
            above = dp[i-1][j]
            if currentCoin <= j and dp[i][j-currentCoin] != -1:
                leftSide = 1 + dp[i][j-currentCoin]
                dp[i][j] = min(above, leftSide) if above != -1 else leftSide
            else:
                dp[i][j] = above
    
    return dp[len(coins)][amount]

testFunc(coinChange)

# Bottom Up Approach, Space Optimized

def coinChange(coins, amount):

    dp = [-1] * (amount + 1)
    dp[0] = 0

    for k in range(1, amount + 1):
        firstCoin = coins[0]
        if k >= firstCoin and dp[k-firstCoin] != -1:
            dp[k] = 1 + dp[k-firstCoin]

    for i in range(1, len(coins) + 1):
        currentCoin = coins[i-1]
        newDP = [-1] * (amount + 1)
        for j in range(amount + 1):
            if j == 0:
                newDP[j] = 0
                continue
            above = dp[j]
            if currentCoin <= j and newDP[j-currentCoin] != -1:
                leftSide = 1 + newDP[j-currentCoin]
                newDP[j] = min(above, leftSide) if above != -1 else leftSide
            else:
                newDP[j] = above
        dp = newDP
    
    return dp[amount]

testFunc(coinChange)


    
            
