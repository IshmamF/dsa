class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        length = len(nums)
        for i in range(1, length):
            prev, currNum = nums[i-1], nums[i]
            if currNum <= prev:
                currSum = 0

            currSum += currNum
            maxSum = max(currSum, maxSum)
        return maxSum