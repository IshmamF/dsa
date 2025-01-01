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