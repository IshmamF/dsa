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
    # curr to hold the current number of subsets
    memo = {}
    def dfs(i, m, n, curr):
        if i >= len(strs) or (m < 0 or n < 0):
            return len(curr)
        if (i, m, n) in memo:
            return memo[(i, m, n)]
        
        count = Counter(strs[i])
        if '1' not in count:
            count['1'] = 0
        elif '0' not in count:
            count['0'] = 0
        
        dontIncludeSubset = dfs(i+1, m, n, curr)
        if n >= count['1'] and m >= count['0']:
            curr.append(strs[i])
            includeSubset = dfs(i+1, m - count['0'], n - count['1'], curr)
            curr.pop()
            memo[(i, m, n)] = max(includeSubset, dontIncludeSubset)
            return memo[(i, m, n)]
        memo[(i, m, n)] = dfs(i+1, m, n, curr)
        return memo[(i, m, n)]

    return dfs(0, m, n, [])

strs = ["10","0001","111001","1","0"]
m, n = 5, 3
output = findMaxForm(strs, m, n)
print(output)

strs = ["10","0","1"]
m, n = 1, 1
output = findMaxForm(strs, m, n)
print(output)