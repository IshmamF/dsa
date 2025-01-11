package twoPointers

import (
    "unicode"
    "strings"
)

func isPalindrome(s string) bool {
    filteredStr := ""
    for _, ascii := range s {
        char := string(ascii)
        if unicode.IsLetter(ascii) {
            filteredStr += strings.ToLower(char)
        } else if unicode.IsNumber(ascii) {
            filteredStr += string(char)
        } 
    }

    L, R := 0, len(filteredStr) - 1
    for L < R {
        if filteredStr[L] != filteredStr[R] {
            return false
        }
        L++
        R--
    }
    return true
}