package arrays

func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)

    for i, num := range nums {
        if val, exists := hashmap[target-num]; exists {
            return []int{i, val}
        }
		hashmap[num] = i
    }
	return []int{-1, -1}
}