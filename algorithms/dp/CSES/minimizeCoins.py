from typing import List
def minimizeCoins(n: int, target: int, coins: List[int]) -> int : 
    '''
    you want to keep adding until you get to target, or we can subtract from target until we hit 0
    base case to consider would be if it hit's target
    we should get the minimum at each iteration within recursive call
    '''
    memo = {}

    def recurse(curr_sum: int, count: int):
        if curr_sum == target:
            return count
        if curr_sum > target:
            return float('inf')
        if (curr_sum, count) in memo:
            return memo[(curr_sum, count)]
        
        minNumCoins = float('inf')
        for coin in coins:
            numWays = recurse(curr_sum+coin, count+1)
            minNumCoins = min(minNumCoins, numWays)

        memo[(curr_sum, count)] = minNumCoins
        return minNumCoins
    
    return recurse(0, 0)

val = minimizeCoins(3, 1000, [1, 3, 5])
print(val)