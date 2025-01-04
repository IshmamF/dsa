## Top 6 Dynamic Programming Patterns
**Video Link:** https://www.youtube.com/watch?v=qMfJegB20BY&ab_channel=MattGuest <br>

### Knapsack Problems
- given a capacity and items (array with each item holding a value and weight)
- decision tree of trying every combination, subtracting every weight from capacity
- in unbounded knapsack, we take the max of: 
  - summing the value at looking left (capacity - current item weight) in our current row and current item value
  - directly above
- in 0/1 knapsack, we check if we can do (capacity - current item weight)
  - If we can, we sum the value at looking diagonally (capacity - current item weight) in the previous row and current item value
  - othewise we use value directly above 

### Grid Based DP Problems
- given a grid where you need to go from one point to another
- each subproblem is a point you reached before getting to the endpoint you're aiming for

### Interval
- Create new subsequence based on a decision
- Seems similar to LCS where we decide to go to next character of string 1 or next character of string 2
- Look out for partitioning, subsequences, subarrays

### Recursive Numbers
- fibonacci type problems

### Palindromic Subsequence
- start at middle value (which is technically a palindrome) and go outwards <- if its odd character length
- if it's even character length, use both middle characters

### Two Sequences
- involves comparing sub sequences in both sequences