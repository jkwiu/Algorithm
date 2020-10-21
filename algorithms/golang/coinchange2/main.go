// 518. Coin Change 2
// You are given coins of different denominations and a total amount of money.
// Write a function to compute the number of combinations that make up that amount.
// You may assume that you have infinite number of each kind of coin.

package main

import "fmt"

func main() {
	arr := []int{1, 3, 5, 7}
	change(10, arr)
}

func change(amount int, coins []int) int {
	arr := make([]int, amount+1)
	arr[0] = 1
	for _, c := range coins {
		if c <= amount {
			for i := 0; i < amount; i++ {
				if i+c <= amount {
					arr[i+c] += arr[i]
				}
			}
		}
	}
	fmt.Println(arr)
	return arr[amount]
}
