package arrays

func isAnagram(s string, t string) bool {
    sMap := make(map[string]int)
    tMap := make(map[string]int)

    for _, c := range s {
        sMap[string(c)] += 1
    }

    for _, c := range t {
        tMap[string(c)] += 1
    }

    for k, v := range sMap {
        if tMap[k] != v { 
            return false 
        }
    }

    for k := range tMap {
        if _, exists := sMap[k]; !exists {
            return false
        }
    }

    return true

}