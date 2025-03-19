'''
there are 6 options , 1...6
base case would be its more than n or equal to n
properly cached, but memory wise, very bad
'''
def diceroll(n: int) -> int:

    memo = {}
    def recurse(val, n):
        if val in memo:
            return memo[val]
        if val > n:
            return 0
        if val == n:
            return 1
        
        count = 0
        for i in range(1, 7):
            memo[val+i] = recurse(val + i, n)
            if memo[val+i] == 0:
                break
            count += memo[val+i]

        return count
        
    return recurse(0, n)

output = diceroll(100)
print(output)



