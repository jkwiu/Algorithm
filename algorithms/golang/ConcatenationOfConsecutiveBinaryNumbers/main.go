// 1680. Concatenation of Consecutive Binary Numbers
// Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

// Example 1:

// Input: n = 1
// Output: 1
// Explanation: "1" in binary corresponds to the decimal value 1.
// Example 2:

// Input: n = 3
// Output: 27
// Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
// After concatenating them, we have "11011", which corresponds to the decimal value 27.
// Example 3:

// Input: n = 12
// Output: 505379714
// Explanation: The concatenation results in "1101110010111011110001001101010111100".
// The decimal value of that is 118505380540.
// After modulo 109 + 7, the result is 505379714.

package main

func main() {
	// println(concatenatedBinary((1)))
	println(concatenatedBinary((3)))
	// println(concatenatedBinary((12)))
	// println(concatenatedBinary((20)))
	// println(concatenatedBinary((42)))
}

func concatenatedBinary(n int) int {
	length, res, mod := 0, 0, 1000000007

	for i := 1; i <= n; i++ {
		if i&(i-1) == 0 { // 자릿수가 올라갈 때 마다 length를 증가
			length++
		}
		res = (res<<length | i) % mod // 자리수만큼 shift이동하고 concat
	}
	return res
}
