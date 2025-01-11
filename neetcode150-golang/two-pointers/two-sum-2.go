package twoPointers

func twoSum(numbers []int, target int) []int {
    L, R := 0, len(numbers)-1
    for L < R {
        sum := numbers[L] + numbers[R]
        if sum > target {
            R--
        } else if sum < target {
            L++
        } else {
            return []int{L+1, R+1}
        }
    }
    return []int{-1, -1}
}