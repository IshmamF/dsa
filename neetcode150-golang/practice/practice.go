package main

import (
	"fmt"
)

func longestOnes(nums []int, k int) int {
    hashmap := make(map[int]int) 
    L := 0
    maxLongest := 0 
    for i := 0; i < len(nums); i++ {
		hashmap[nums[i]] += 1

        for hashmap[0] > k {
            hashmap[nums[L]] -= 1
            L += 1
        }

		maxLongest = max(maxLongest, hashmap[1] + hashmap[0])
    }
    return maxLongest
}

func main() {
	test1 := []int{0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1}
	test2 := []int{0,0,0,1}
	k1 := 3
	k2 := 4
	output1 := longestOnes(test1, k1)
	fmt.Println(output1)
	output2 := longestOnes(test2, k2)
	fmt.Println(output2)

}