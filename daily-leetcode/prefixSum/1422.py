# Problem Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01

def maxScore(s: str) -> int:
    '''
    Get prefix sum of 0s and postfix sum of 1s
    [1, 1, 1, 1, 2, 2]
    [4, 4, 3, 2, 1, 1]

    [1, 2, 2, 2, 2]
    [3, 3, 3, 2, 1]

    [0, 0, 0, 0]
    [4, 3, 2, 1]
    '''
    zeros, ones = [0] * len(s), [0] * len(s)
    countZeros, countOnes, maxScore = 0, 0, 0
    for i in range(len(s)):
        left = s[i]
        right = s[-(i + 1)]

        if left == '0':
            countZeros += 1
        if right == '1':
            countOnes += 1
        
        zeros[i] = countZeros

        ones[-(i + 1)] = countOnes
    for i in range(len(s) - 1):
        maxScore = max(maxScore, zeros[i] + ones[i+1])
    return maxScore