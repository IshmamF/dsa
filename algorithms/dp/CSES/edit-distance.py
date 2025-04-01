str1 = input()
str2 = input()
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    memo = {}
    def helper(i, j, m, n):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == m:
            return abs(n - j)
        if j == n:
            return abs(m - i)
        
        if str1[i] != str2[j]:
            memo[(i, j)] = 1 + min(helper(i+1, j, m, n), helper(i, j+1, m, n), helper(i+1, j+1, m, n))
            return memo[(i, j)]
        else:
            memo[(i, j)] = helper(i+1, j + 1, m, n)
            return memo[(i, j)]
        
    return helper(0, 0, m, n)
print(edit_distance(str1, str2))