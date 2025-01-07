# https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03


def waysToSplitArray(nums: List[int]) -> int:
    lastIndex = len(nums) - 1
    totalSum = sum(nums)
    count = 0

    currSum = 0
    for i in range(lastIndex):
        currSum += nums[i]
        rightSum = totalSum - currSum
        if currSum >= rightSum:
            count += 1

    return count