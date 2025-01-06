# Top Down Memoized Solution
def change(amount, coins):
    memo = {}

    def dfs(i, current):

        if i == len(coins):
            return 1 if current == amount else 0
        if current > amount:
            return 0
        if (i, current) in memo:
            return memo[(i, current)]

        skip = dfs(i + 1, current)
        include = dfs(i, current + coins[i])
        memo[(i, current)] = skip + include
        return skip + include

    return dfs(0, 0)

# Bottom Up Approach
'''
Bounds: 
    i : 0 -> length of coins 
    current : 0 -> amount
Side note, when create dp, we need to add 1 to each so we can index the values 
Order:
    - look at recursive calls
    skip = dfs(i + 1, current)
    include = dfs(i, current + coins[i])

    with skip, i is changing, current is constant
    with include, i is constant, current is changing

    i + 1 > i , means we need to calculate big before small so reverse order
    current + coins[i] > current means we need to calculate big before small 
    so reverse order as well 
Create DP table with bounds 
Remove memo, and replace recursive calls with dp table (you'd use the parameters)
as the index values
Create for loops using Order and call your recursive call at each iteration
We can then add the rercursive implementation into our iteration. Instead of returning,
we assign to current position of table.
To remove base case, we can preprocess array, assigning everything to 0 and assigning last
index (bottom right corner) to 1. 
To optimize approach, we see that i is changing constantly. We can use a 1D array instead of 2D.
'''
def change(amount, coins):
    #dp = [[None]*(amount + 1) for _ in range(len(coins)+1)]
    dp = [0]*(amount + 1)
    dp[amount] = 1

    """
    No longer need the recursive function
    def dfs(i, current):

        if i == len(coins):
            return 1 if current == amount else 0

        skip = dp[i + 1][current]
        include = 0
        if current + coins[i] <= amount:
            include = dp[i][current + coins[i]]

        return skip + include
    """

    for i in range(len(coins)-1, -1, -1):
        new_dp = [0]*(amount + 1)
        for j in range(amount, -1, -1):

            skip = dp[j] # uses previous row aka initial dp
            include = 0
            if j + coins[i] <= amount:
                include = new_dp[j + coins[i]] # works on current row aka new dp

            new_dp[j] = skip + include
        dp = new_dp
    return new_dp[0]

print(change(5, [1,2,5]))