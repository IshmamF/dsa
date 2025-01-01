package arrays

import (
	"container/heap"
)

type Tuple struct {
	frequency int
	element int
}

type maxHeap []Tuple

func (h maxHeap) Len() int {
	return len(h)
}

func (h maxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}	

func (h maxHeap) Less(i, j int) bool {
	return h[i].frequency > h[j].frequency
}

func (h *maxHeap) Push(x any) {
    *h = append(*h, x.(Tuple))
}

func (h *maxHeap) Pop() any {
    old := *h
    n := len(old)
    poppedVal := old[n-1]
    *h = old[0 : n-1]
    return poppedVal
}

/*
Create a tuple data structure, and then a type for a list of that data structure
Implement methods len, swap, push, less, pop functions
Create hashmap, go through nums and count frequency for each element
Go through hashmap, push a tuple that uses each key and value 
Iterate up to k times, popping from the heap and adding to a list of ints
Return that list
*/

func topKFrequent(nums []int, k int) []int {
    h := &maxHeap{}
    heap.Init(h)
	elementMap := make(map[int]int)
	for _, elmt := range nums {
		elementMap[elmt] += 1
	}

	for key, val := range elementMap {
		temp := Tuple{
			frequency: val,
			element: key,
		}
		heap.Push(h, temp)
	}


	var output []int
	for i := 0; i < k; i++ {
		if len(*h) == 0 {
			break
		}
		val := heap.Pop(h).(Tuple)
		output = append(output, val.element)
	}
	return output
}