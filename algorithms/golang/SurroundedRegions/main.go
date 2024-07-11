// Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

// Example 1:

// Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
// Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
// Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
// Example 2:

// Input: board = [["X"]]
// Output: [["X"]]
// Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
// Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
// Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

package main

import "fmt"

func main() {
	input := [][]string{{"X", "X", "X", "X"}, {"X", "O", "O", "X"}, {"X", "X", "O", "X"}, {"X", "O", "X", "X"}}
	for _, v := range input {
		for _, v2 := range v {
			print(v2)
		}
		println()
	}

	// input의 가로 길이
	inputRowLen := len(input[0])
	// input의 세로 길이
	inputColLen := len(input)
	// 주위 X의 좌표리스트
	nearXList := [][]int{}
	// 주위 X의 갯수
	nearXTotalCnt := len(nearXList)
	// 인접한 O의 좌표리스트
	nearOList := [][]int{}
	// 인접한 O들의 갯수
	nearOTotalCnt := len(nearOList)
	// 주위 X의 갯수가 인접한 O의 갯수에 4를 더한 값이면 둘러쌓인 것으로 판단
	if nearOTotalCnt+4 == nearXTotalCnt {
		println("둘러쌓임")
	}

	// 첫 O를 찾기 위한 서치
	for i, v := range input {
		for j, v2 := range v {
			if v2 == "O" {
				fmt.Printf("o의 좌표: (%d, %d)\n", i, j)
				nearOList = append(nearOList, []int{i, j})
			}
		}
	}

	// 첫 O부터 시작해서 반시계방향으로 주위요소 체크
	if nearOList[0][0] == 0 {
		println("위쪽이 뚫려있음")
	}
	if nearOList[0][1] == 0 {
		println("왼쪽이 뚫려있음")
	}
	if nearOList[0][1] == inputRowLen-1 {
		println("오른쪽이 뚫려있음")
	}
	if nearOList[0][1] == inputColLen-1 {
		println("아래쪽이 뚫려있음")
	}

	for _, v := range nearOList {
		for i := 0; i < len(v); i++ {
			// 위
			fmt.Printf("(%d, %d)의 위는 %s\n", v[0], v[1], input[v[0]-1][v[1]])
			if input[v[0]-1][v[1]] == "X" {
				// 왼쪽
				fmt.Printf("(%d, %d)의 왼쪽은 %s\n", v[0], v[1], input[v[0]][v[1]-1])
				if input[v[0]][v[1]-1] == "X" {
					// 아래
					fmt.Printf("(%d, %d)의 아래쪽은 %s\n", v[0], v[1], input[v[0]+1][v[1]])
					if input[v[0]+1][v[1]] == "X" {
						// 오른쪽
						fmt.Printf("(%d, %d)의 아래쪽은 %s\n", v[0], v[1], input[v[0]][v[1]+1])
					}
				} else {
					fmt.Printf("(%d, %d)의 아래쪽은 %s\n", v[0], v[1], input[v[0]][v[1]+1])
				}
			}
			break
		}
	}
}

func solve(board [][]byte) {

}
