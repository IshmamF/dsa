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