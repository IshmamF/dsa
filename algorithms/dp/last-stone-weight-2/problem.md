**Problem Link:** https://leetcode.com/problems/last-stone-weight-ii/description/

## Thought Process:
- Initially, I thought we can probably have an i and j index to try every combination. However, that's very complicated since we need to keep track of what values we visited for i and j, the result computed , and so on. 
- The better way to think about this problem is that let's say we start at 0, and for every stone, we decide to either add or subtract the current stone. If we add the current stone and subtract the next stone, that's effectively doing what I wanted earlier to try every combination of subtracting two stones together.
- The solution then looks very similar to Top Down Memoization Solution for Target Sum except for base cases, and we return the minimum of our two recursive calls. 
- Our base case would be if we went through all the stones. If the result is negative or greater than the sum of all the stones, we ignore it (aka return infinity), otherwise we return the result.

## Neetcode

### Top Down Memoization
- Pretty much we can break the stones into two subsets, and we want to minimize the difference between the subsets
- Instead of subtracting or adding, we decide to either add the current stone or not add the stone to build one subset
- The target would be the ceiling of sum of all stones divided by 2
- Our base case is essentially if we used all stones or if we got value greater than or equal to target, in which case we do <br>
abs(total - (sum - total)), where total is the value we built up <br>
Doing the sum - total, gives us the other subset. And doing the difference between total (subset we built) and the other subset, gives us the smallest stone weight left (ofcourse we'd have to use minimum function to check we're getting the minimum from our recursive calls). <br>
Absolute value is necessary incase the difference becomes negative (which is plausible). <br>
- It's similar to partition sum problem so doing bottom up approach or using hashsets should follow the same patterns. 