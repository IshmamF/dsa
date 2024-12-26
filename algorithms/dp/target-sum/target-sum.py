# Problem Link: https://leetcode.com/problems/target-sum/

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
