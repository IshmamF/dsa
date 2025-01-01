# Problem Link: https://leetcode.com/problems/ones-and-zeroes/

'''
We want to create the biggest possible subset, given m 0s and n 1s. 
We need to decide if we want to include a string or not include a string, which impacts our m and n
Possible base cases is if either m or n are less than or equal to 0, and if we reach the end of the list

'''

# My Solution
from collections import Counter
def findMaxForm(strs, m, n):
    # i for index
    # m for number of 0s left
    # n for number of 1s left
    hashmap = {}

    for i, s in enumerate(strs):
        hashmap[i] = Counter(s)

    memo = {}
    def dfs(i, m, n):
        if i >= len(strs):
            return 0
        if (i, m, n) in memo:
            return memo[(i, m, n)]
        
        count = hashmap[i]
        zeros = count.get('0', 0)
        ones = count.get('1', 0)
        
        dontIncludeSubset = dfs(i+1, m, n)

        includeSubset = float("-inf")
        if n >= ones and m >= zeros:
            includeSubset = 1 + dfs(i+1, m - zeros, n - ones)

        memo[(i, m, n)] = max(includeSubset, dontIncludeSubset)
        return memo[(i, m, n)]

    return dfs(0, m, n)

strs = ["10","0001","111001","1","0"]
m, n = 5, 3
output = findMaxForm(strs, m, n)
print(output)

strs = ["10","0","1"]
m, n = 1, 1
output = findMaxForm(strs, m, n)
print(output)

# Neetcode Bottom Up Approach

def findMaxForm(strs, m, n):
    arr = [[0] * 2 for _ in range(len(strs))]
    for i, s in enumerate(strs):
        for c in s:
            arr[i][ord(c) - ord('0')] += 1

    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
    print(dp)

    for i in range(1, len(strs) + 1):
        for j in range(m + 1):
            for k in range(n + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= arr[i - 1][0] and k >= arr[i - 1][1]:
                    dp[i][j][k] = max(dp[i][j][k], 1 + dp[i - 1][j - arr[i - 1][0]][k - arr[i - 1][1]])

    return dp[len(strs)][m][n]

strs = ["10","0","1"]
m, n = 1, 1
output = findMaxForm(strs, m, n)
print(output)