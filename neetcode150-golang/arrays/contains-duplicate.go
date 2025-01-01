package arrays

import (
    "slices"
)

/*
Sort the array, and check if the previous value is the same as current value
*/

func containsDuplicate(nums []int) bool {
        slices.Sort(nums) 
        for i := 1; i < len(nums); i++ {
            if nums[i-1] == nums[i] {
                return true
            }
        }
        return false
}