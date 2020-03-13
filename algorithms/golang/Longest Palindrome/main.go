package main

import "fmt"

// Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
//This is case sensitive, for example "Aa" is not considered a palindrome here.
//Note:
//Assume the length of given string will not exceed 1,010.
/*
Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
*/

// rune:int 의 map m을 만든다.
// 각 글자를 키값으로 설정하여, 각 키에 같은 값의 글자가 나오면, 같은 글자가 나온 횟수를 카운트한다
func main() {
	count := longestPalindrome("aaadccbdbc")
	fmt.Printf("Longest Palindrome(가장 긴 회문)의 길이는 %d입니당.", count)
}

func longestPalindrome(s string) int {
	m := make(map[rune]int)
	for _, char := range s {
		m[char] += 1
	}

	count := 0

	// 반으로 포갰을 때 중심이 되는 글자가 있으면 center 는 true, 중심의 글자 1개를 카운트에 더한다.
	center := false

	// s string의 각 글자를 rune형으로 변환하여 mapping한다.
	for _, each := range m {
		// 각 글자를 반으로 접었을 때의 반쪽의 글자 수의 총합
		count += each / 2

		//어떤 글자가 홀수개이면 중심점 스위치를 on 한다.
		if each%2 == 1 {
			center = true
		}
	}

	//총 길이
	count = 2 * count

	//중심점의 갯수까지 합친다.
	if center == true {
		count++
	}

	return count
}
