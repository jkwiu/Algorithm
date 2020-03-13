/*
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
*/
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

import "strconv"

func main() {

}

func binaryTreePaths(root *TreeNode) []string {
	result := []string{}
	var helper func(*TreeNode, string)
	helper = func(root *TreeNode, path string) {
		if root == nil {
			return
		}
		val := strconv.Itoa(root.Val)
		if path == "" {
			path = val
		} else {
			path = path + "->" + val
		}
		if root.Left == nil && root.Right == nil {
			result = append(result, path)
			return
		}
		helper(root.Left, path)
		helper(root.Right, path)
		return
	}
	helper(root, "")
	return result
}
