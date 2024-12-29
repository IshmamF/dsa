package main

import (
	"fmt"
)

func counter(str string) map[string]int {
	m := make(map[string]int)
	for _, char := range str {
		m[string(char)] += 1
	}
	return m
}

func main() {
	m := counter("hello")
	fmt.Println(m)

}