package arrays

import (
    "strings"
	"sort"
)

/*
Go through array, sort string, use the sorted string as key for hashmap,
add original string to the list (value of the sorted string)

Go through hashmap, add the value (list of strings) to a list
return that list after iteration is done
*/


func groupAnagrams(strs []string) [][]string {
    hashmap := make(map[string][]string)

	for _, s := range strs {
		unsortedChars := strings.Split(s, "")
		sort.Slice(unsortedChars, func(i, j int) bool {
			return unsortedChars[i] < unsortedChars[j]
		})
		sortedString := strings.Join(unsortedChars, "")
		hashmap[sortedString] = append(hashmap[sortedString], s)
	}

	var values [][]string

	for _, val := range hashmap {
		values = append(values, val)
	}

	return values
}