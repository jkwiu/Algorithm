/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*/

//한글의 길이가 3이 나오는 이유 => 참고하면 좋은 링크 : http://pyrasis.com/book/GoForTheReallyImpatient/Unit45/02
//영문자를 저장할 때는 문자 하나가 1바이트를 차지합니다.
//하지만 한글, 한자, 일본어 같은 문자는 1바이트로 저장할 수가 없기 때문에
//보통 2바이트로 저장합니다(Multi Byte Character Set, MBCS). UTF-8은 가변 길이 문자 인코딩 방식이라 문자를 저장할 때
//1바이트에서 4바이트까지 사용하며 한글은 3바이트로 저장합니다.
package main

import (
	"fmt"
)

func main() {
	s := []string{"a spa    c e fgjfgjinnn  iiiii"}
	for i := 0; i < len(s); i++ {
		fmt.Println(lengthOfLastWord(s[i]))
	}
	//rst := lengthOfLastWord(s)
	//fmt.Println(rst)
}

func lengthOfLastWord(s string) int {
	//끝에부터 읽는다, 빈칸이 나올 때까지
	//빈칸이 나오면 스위치를 ON
	//스위치가 ON되면 글자수를 Count한다.
	//끝에부터 읽는다, 빈칸이 나올 때까지
	emptyIsNow := false
	indx, rst := 0, 0
	for i := range s {
		i = len(s) - 1 - i
		if s[i] == 32 {
			//빈칸이 나오면 스위치를 ON
			emptyIsNow = true
			indx = i + 1
			break
		}
	}
	//스위치가 ON되면 글자수를 Count한다. OFF는 빈칸이 없는 것
	if emptyIsNow {
		rst = len(s[indx:])
	} else {
		rst = len(s)
	}
	return rst
}
