from collections import defaultdict
from typing import List, DefaultDict
def coinCombination2(n: int, target: int, coins: List[int]) -> int:
    '''
    similar to coin combination 1 but im not sure how to keep track of duplicates
    i think the only way is a hashmap?
    '''
    memo = {}
    valid_count = []
    def recurse(curr_sum: int, curr_count: DefaultDict):
        if curr_sum == target:
            if curr_count in valid_count:
                return 0
            valid_count.append(curr_count)
            return 1
        if curr_sum > target:
            return 0
        if curr_sum in memo:
            return memo[curr_sum]
        
        numWays = 0
        for coin in coins:
            copy = curr_count.copy()
            copy[coin] += 1
            numWays += recurse(curr_sum+coin, copy)

        memo[curr_sum] = numWays
        return numWays 

    return recurse(0, defaultdict(int))


val = coinCombination2(3, 9, [2, 3, 5])
print(val)
