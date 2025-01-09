# Problem Link: https://leetcode.com/problems/minimum-cost-for-tickets/

"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
- a number in days represent the day of the year you will travel

Train tickets are sold in three different ways:
a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
- 3 decisions
- maybe greedy?

The passes allow that many days of consecutive travel


For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
"""
from typing import List

# My Solutions

# Top Down Memoized Recursive Solution:
def mincostTickets(days: List[int], costs: List[int]) -> int:
    memo = {}
    def helper(i, day):
        while i < len(days) and day >= days[i]:
            i += 1
        if i == len(days):
            return 0
        if (i, day) in memo:
            return memo[(i, day)]
        else:
            daily = helper(i+1, days[i]) + costs[0]
            weekly = helper(i+1, days[i] + 6) + costs[1]
            monthly = helper(i+1, days[i] + 29) + costs[2]
        minimum = min(daily, weekly, monthly)
        memo[(i, day)] = minimum 
        return minimum
    return helper(0, 0)

# Bottom Up Iterative
def mincostTickets(days: List[int], costs: List[int]) -> int:
    """
    Bounds: 
    i : [0, len(days)]
    day : [1, 365]

    Order:
    i : i + 1
        big before small
        gotta go in reverse order
    day : +6 or + 29
        big before small
        reverse order as well
    """
    #memo = {}
    dp = [[0]*366 for _ in range(len(days)+1)]
    def helper(i, day):
        while i < len(days) and day >= days[i]:
            i += 1
        if i == len(days):
            return 0
        else:
            weeklyIndex = days[i] + 6 if days[i] + 6 < 366 else 365
            monthlyIndex = days[i] + 29 if days[i] + 29 < 366 else 365

            daily = dp[i+1][days[i]] + costs[0]
            weekly = dp[i+1][weeklyIndex] + costs[1]
            monthly = dp[i+1][monthlyIndex] + costs[2]

            minimum = min(daily, weekly, monthly)
        return minimum

    for i in range(len(days), -1, -1):
        for j in range(365, -1, -1):
            dp[i][j] = helper(i, j)

    return dp[0][0]

# Neetcode Solutions