# Problem Link: https://leetcode.com/problems/ones-and-zeroes/

'''
We want to create the biggest possible subset, given m 0s and n 1s. 
We need to decide if we want to include a string or not include a string, which impacts our m and n
Possible base cases is if either m or n are less than or equal to 0, and if we reach the end of the list

'''
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