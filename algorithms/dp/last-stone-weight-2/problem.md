**Problem Link:** https://leetcode.com/problems/last-stone-weight-ii/description/

## Thought Process:
- Initially, I thought we can probably have an i and j index to try every combination. However, that's very complicated since we need to keep track of what values we visited for i and j, the result computed , and so on. 
- The better way to think about this problem is that let's say we start at 0, and for every stone, we decide to either add or subtract the current stone. If we add the current stone and subtract the next stone, that's effectively doing what I wanted earlier to try every combination of subtracting two stones together.
- The solution then looks very similar to Top Down Memoization Solution for Target Sum except for base cases, and we return the minimum of our two recursive calls. 
- Our base case would be if we went through all the stones. If the result is negative or greater than the sum of all the stones, we ignore it (aka return infinity), otherwise we return the result.

## Neetcode
