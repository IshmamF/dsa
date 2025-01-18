package dp

var memo = make(map[int]int)

func climbStairs(n int) int {
    if n == 1 {
        return 1
    } else if n == 2 {
        return 2
    } else if val, exists := memo[n]; exists {
        return val
    }

    value := climbStairs(n-1) + climbStairs(n-2)
    memo[n] = value
    return value
}