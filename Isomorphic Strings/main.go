//Given two strings s and t, determine if they are isomorphic.
//Two strings are isomorphic if the characters in s can be replaced to get t.
//All occurrences of a character must be replaced with another character while
//preserving the order of characters. No two characters may map to the same character but a character may map to itself.

package main

import "fmt"

func main() {
	isIsomorphicArray("egg", "add")
	isIsomorphicArray("egg", "adg")

	isIsomorphicMap("egg", "add")
	isIsomorphicMap("egg", "adg")
}

//sol 1
//mapping을 이용하는 방법, 시간 복잡도 log2N
func isIsomorphicMap(s, t string) bool {
	stmap := make(map[byte]byte)
	tsmap := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		a, b := s[i], t[i]
		if other, ok := stmap[a]; ok {
			if other != b {
				fmt.Println("false")
				return false
			}
		} else if other, ok := stmap[b]; ok {
			if other != a {
				fmt.Println("false")
				return false
			}
		} else {
			stmap[a] = b
			tsmap[b] = a
		}
	}
	fmt.Println("true")
	return true
}

//sol2 array를 이용
// 1글자는 아스키코드로 1byte로 표현되며
// 0~256 byte이므로, 256배열을 만들어주면
//시간복잡도가 O(1)이 된다.
func isIsomorphicArray(s, t string) bool {
	stmap := make([]byte, 256)
	tsmap := make([]byte, 256)

	for i := 0; i < len(s); i++ {
		a, b := s[i], t[i]
		if stmap[a] != 0 {
			if stmap[a] != b {
				fmt.Println("false")
				return false
			}
		} else if tsmap[b] != 0 {
			if tsmap[b] != a {
				fmt.Println("false")
				return false
			}
		} else {
			stmap[a] = b
			tsmap[b] = a
		}
	}
	fmt.Println("true")
	return true
}
