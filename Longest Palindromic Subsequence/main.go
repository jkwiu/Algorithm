/*
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
*/

package main

import "fmt"

func longestPalindromeSubseq(s string) int {

	//Input
	// Input: "abbcbbccbae" 10
	// Output: "abbcbba"  7
	// 와리가리 전법?
	mvarray := make([]rune, len(s))
	for i, mv := range s {
		mvarray[i] = mv
	}
	fmt.Println(mvarray)
	pali := make([]rune, len(mvarray))
	fmt.Println(pali)

	//중심점 문제는 나중에
	for i := 0; i < len(mvarray)/2; i++ {
		for j := len(mvarray); j > i; j-- {
			if mvarray[i] == mvarray[j] {
				pali[i], pali[len(pali)-i] = mvarray[i], mvarray[j]
				break
			}
		}
	}

	return 0
}

func main() {
	longestPalindromeSubseq("abbcbbccbae")
}
