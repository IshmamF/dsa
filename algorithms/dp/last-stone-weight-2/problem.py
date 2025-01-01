# Problem Link: https://leetcode.com/problems/last-stone-weight-ii/description/

# My solution
def lastStoneWeightII(stones):
        
    if len(stones) == 1:
        return stones[0]
        
    totalSum = sum(stones)
    memo = {}

    def helper(i, possibleSum):
        if i == len(stones):
            if possibleSum < 0 or possibleSum >= totalSum:
                return float('inf')
            else:
                return possibleSum
        if (i, possibleSum) in memo:
            return memo[(i, possibleSum)]
                
        addStone = helper(i+1, possibleSum + stones[i])
        subStone = helper(i+1, possibleSum - stones[i])
        memo[(i, possibleSum)] = min(addStone, subStone)
        return memo[(i, possibleSum)]
    
    return helper(0, 0)

stones = [2,7,4,1,8,1]
output = lastStoneWeightII(stones)
print(output)

stones = [31,26,33,21,40]
output = lastStoneWeightII(stones)
print(output)

# Neetcode Top Down Solution

def lastStoneWeightII(stones):
    stoneSum = sum(stones)
    target = (stoneSum + 1) // 2
    dp = {}

    def dfs(i, total):
        if total >= target or i == len(stones):
            return abs(total - (stoneSum - total))
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
        return dp[(i, total)]

    return dfs(0, 0)