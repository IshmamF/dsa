package main

func Counter(str string) map[string]int {
    m := make(map[string]int)
    for _, c := range str {
        m[string(c)]++
    }
    return m
}

type key struct {
	i, m, n int
}

func findMaxForm(strs []string, m int, n int) int {
	hashmap := make(map[int]map[string]int)
    for i, s := range strs {
		hashmap[i] = Counter(s)
	}

	memo := make(map[key]int)
	var dfs func(i, m, n int) int
	dfs = func (i int, m int, n int) int {
		if i == len(strs) {
			return 0
		}
		temp_key := key{i: i, m: m, n: n}
		if value, exists := memo[temp_key]; exists {
			return value
		}

		count := hashmap[i]
		zeros := count["0"]
		ones := count["1"]

		DontInclude := dfs(i+1, m, n)
		Include := -1
		if m >= zeros && n >= ones {
			Include = 1 + dfs(i+1, m - zeros, n - ones)
		}
		memo[temp_key] = max(Include, DontInclude)
		return memo[temp_key]
	}
	return dfs(0,m,n)
}

