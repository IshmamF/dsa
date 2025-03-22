
def diceroll(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1 

    for count in range(1, n+1):
        for roll in range(1, 7):
            if roll > count:
                break
            dp[count] += dp[count - roll]

    return dp[n]