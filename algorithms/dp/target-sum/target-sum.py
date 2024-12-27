# Problem Link: https://leetcode.com/problems/target-sum/

test = [1, 1, 1, 1, 1]

# My Optimal solution:
from collections import defaultdict

def findTargetSumWays(nums, target):

    prevList = {0: 1}

    for n in nums: 
        currList = defaultdict(int)
        for key,val in prevList.items(): 
            addValue = key + n 
            subtractValue = key - n

            currList[addValue] += val
            currList[subtractValue] += val
            
        prevList = currList
    return prevList[target]

print(findTargetSumWays(test, 3))

# My Brute Force Solution:
def findTargetSumWays(nums, target):
    def helper(i, target, count):
        if i >= len(nums):
            if target == 0:
                count[0] += 1 
            return 

        addVal = target + nums[i]
        subVal = target - nums[i]

        helper(i + 1, addVal, count)
        helper(i + 1, subVal, count)

    count = [0]
    helper(0, target, count)
    return count[0]

print(findTargetSumWays(test, 3))

# Neetcode's Brute Force Solution:
def findTargetSumWays(nums, target):
    def dfs(i, target):
        if i >= len(nums):
            return 1 if target == 0 else 0
        return dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])

    return dfs(0, target)

print(findTargetSumWays(test, 3))

# Neetcode Top Down Memoization Solution:
def findTargetSumWays(nums, target):
    memo = {}
    def dfs(i, target):
        if i >= len(nums):
            return 1 if target == 0 else 0
        if (i, target) in memo:
            return memo[(i, target)]
        
        memo[(i, target)] = dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])
        return dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])

    return dfs(0, target)

print(findTargetSumWays(test, 3))