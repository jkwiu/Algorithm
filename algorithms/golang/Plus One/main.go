//Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
//The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
//You may assume the integer does not contain any leading zero, except the number 0 itself.

package main

import "fmt"

func main() {
	digits := []int{9}
	rst := plusOne(digits)
	fmt.Println(rst)
}

/* sol1 은 큰 숫자를 표현못함. int64가 아무리 커도
엄청 큰 숫자를 표현할 수 없어서 이 솔루션은 안됨
func plusOne(digits []int) []int {
	n := ConvertInt(digits)

	n++

	return ConvertIntArray(n)
}

func ConvertInt(digits []int) int {
	// 1, 2, 3  -> 123
	no := 0
	for i := 0; i < len(digits); i++ {
		no *= 10
		no += digits[i]
	}
	return no
}

func ConvertIntArray(n int) []int {
	rst := make([]int, 0)
	for n > 0 {
		d := n % 10
		rst = append([]int{d}, rst...)
		n /= 10
	}
	return rst
}

*/

func plusOne(digits []int) []int {
	//[1,2,3] -> [1,2,4]
	//[9,9] -> [0, 0]이 아니고 [9,9] -> [1, 0, 0]
	//carry는 올림수
	carry := true
	for i := len(digits) - 1; i >= 0; i-- {
		if carry {
			if digits[i] == 9 {
				digits[i] = 0
				carry = true
			} else {
				digits[i]++
				carry = false
			}
		} else {
			break
		}
	}

	if carry {
		digits = append([]int{1}, digits...)
	}
	return digits
}
