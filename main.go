package main

import "fmt"

func main() {
	progresses := []int{93, 30, 55}
	speeds := []int{1, 30, 5}
	ans := solution(progresses, speeds)
	fmt.Println(ans)
}

func solution(progresses []int, speeds []int) []int {
	var workday []int

	workday = make([]int, len(progresses))

	for i := 0; i < len(progresses); i++ {
		workday[i] = (100 - progresses[i]) / speeds[i]
	}

	var ans []int
	ans = make([]int, 0)

	cnt := 0
	fix := 0

	for i := 0; i < len(workday); i++ {
		if fix >= workday[i] {
			cnt++
		} else {
			fix = workday[i]
			if i != 0 {
				ans = append(ans, cnt)
			}
			cnt = 1
		}

		if i == len(workday)-1 {
			ans = append(ans, cnt)
		}
	}
	return ans
}
