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

            
