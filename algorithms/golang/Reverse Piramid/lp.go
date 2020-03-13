package main

import "fmt"

func main() {
	for i := 0; i < 3; i++ {
		for j := 0; j < i; j++ {
			fmt.Print(" ")
		}
		for k := 5; k > 2*i; k-- {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
