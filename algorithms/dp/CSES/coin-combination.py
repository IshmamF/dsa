from typing import List
def coinCombination(n: int, target: int, coins: List[int]) -> int:
    '''
    similar to minimize coins but everytime we hit target, we return 1
    '''
    memo = {}
    def recurse(curr_sum: int):
        if curr_sum == target:
            return 1
        if curr_sum > target:
            return 0
        if curr_sum in memo:
            return memo[curr_sum]
        
        numWays = 0
        for coin in coins:
            numWays += recurse(curr_sum+coin)

        memo[curr_sum] = numWays
        return numWays 
    
    return recurse(0)

val = coinCombination(3, 100, [2, 3, 5])
print(val)