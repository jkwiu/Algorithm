// Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

// Note:

// Your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution and you may not use the same element twice.
// Example:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

package main

import "fmt"

func main() {

	nums := []int{2, 7, 11, 15}
	target := 18

	rst := twoSum(nums, target)
	fmt.Println(rst)
}

// func twoSum(numbers []int, target int) []int {

// 	rst := []int{}

// 	for i := 0; i < len(numbers); i++ {
// 		for j := i + 1; j < len(numbers); j++ {
// 			if numbers[i]+numbers[j] == target {
// 				rst = []int{i + 1, j + 1}
// 			}
// 		}
// 	}
// 	return rst
// }

// binary search
func twoSum(numbers []int, target int) []int {
	var i, j int
	for i = 0; i < len(numbers); i++ {
		j = search(numbers, target-numbers[i], i+1, len(numbers)-1)
		if j != -1 {
			break
		}
	}

	return []int{i + 1, j + 1}
}

func search(numbers []int, target, start, end int) int {
	for start <= end {
		mid := (start + end) / 2
		if numbers[mid] == target {
			return mid
		} else if numbers[mid] > target {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}

	return -1
}
