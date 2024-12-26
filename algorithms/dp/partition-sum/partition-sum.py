# Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/description/

# Neetcode Solutions

# Brute Force:
def canPartition(nums):
    if sum(nums) % 2: # if sum is odd, return False
        return False
    
    def dfs(i, target):
        # we overshot the target and it's not possible to reach it
        # or
        # we never reach the target after going through all the indexes
        if target < 0 or i >= len(nums):
            return False
        
        if target == 0: # we hit the target
            return True
        
        return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
    
    return dfs(0, sum(nums) // 2)

test = [1, 5, 11, 5]
print(canPartition(test)) # True
test = [1, 2, 3, 5]
print(canPartition(test)) # False

# Optimization:
"""
Pretty much the same as the brute force solution, but we add memoization to avoid recomputing the same subproblems.
"""
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    n = len(nums)
    memo = [[-1] * (target + 1) for _ in range(n + 1)]

    def dfs(i, target):
        if target == 0:
            return True
        if i >= n or target < 0:
            return False
        if memo[i][target] != -1:
            return memo[i][target]
        
        memo[i][target] = (dfs(i + 1, target) or 
                            dfs(i + 1, target - nums[i]))
        return memo[i][target]

    return dfs(0, target)


test = [1, 5, 11, 5]
print(canPartition(test)) # True
test = [1, 2, 3, 5]
print(canPartition(test)) # False

# Tabulation:
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # If we arent using any elements, we can't reach any target sum
    # so the first row except for dp[0][0] is False
    # dp[i][0] is True because we can reach the target sum of 0 by not using any elements
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j: # if target is greater than the current number
                dp[i][j] = (dp[i - 1][j] or # look at cell at previous row and same column
                            dp[i - 1][j - nums[i - 1]]) # check if we can reach the target sum by using the current number
            else:
                # if current number is greater than target sum, we can't use it but it's possible to reach the target sum without it
                # since previous items can add up to the target sum
                dp[i][j] = dp[i - 1][j] 

    return dp[n][target] 
test = [1, 5, 11, 5]
print(canPartition(test)) # True
test = [1, 2, 3, 5]
print(canPartition(test)) # False

# Space Optimized Tabulation:
def canPartition(nums):
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    prevDp = [False] * (target + 1) # previous row
    nextDp = [False] * (target + 1) # current row

    prevDp[0] = True 
    for i in range(len(nums)):
        for j in range(1, target + 1):
            if j >= nums[i]:
                nextDp[j] = prevDp[j] or prevDp[j - nums[i]]
            else:
                nextDp[j] = prevDp[j]
        prevDp = nextDp # update previous row to current row
        
    return nextDp[target]
test = [1, 5, 10, 1, 5]
print(canPartition(test)) # True
test = [1, 2, 3, 5]
print(canPartition(test)) # False