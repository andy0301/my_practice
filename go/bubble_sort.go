package main

import (
	"fmt"
	"math/rand"
)

func bubble_sort(A []int) []int {
	len := len(A)
	for i := 0; i < len; i++ {
		for j := i + 1; j < len-i; j++ {
			if A[i] > A[j] {
				A[i], A[j] = A[j], A[i]
			}
		}
	}

	return A

}

func main() {
	len := 10
	A := make([]int, len)
	for i := 0; i < len; i++ {
		A[i] = rand.Intn(100)
	}
	fmt.Println(A)
	fmt.Println(bubble_sort(A))

}
