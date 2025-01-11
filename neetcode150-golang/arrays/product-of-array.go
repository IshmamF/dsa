package arrays

func productExceptSelf(nums []int) []int {
    numsLen := len(nums)

    var prefix []int
    postfix := make([]int, numsLen)

    curr := 1
    for _, num := range nums {
        curr *= num
        prefix = append(prefix, curr)
    }
    curr = 1
    for i := numsLen-1; i > -1; i-- {
        curr *= nums[i]
        postfix[i] = curr
    }

    var res []int
    for i, _ := range nums {
        if i == 0 {
            res = append(res, postfix[i+1])
        } else if i == numsLen - 1 {
            res = append(res, prefix[i-1])
        } else {
            left := prefix[i-1]
            right := postfix[i+1]
            res = append(res, left * right)
        }
    }
    return res
}