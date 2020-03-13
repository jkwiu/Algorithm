//Given a binary tree, find its maximum depth.
//The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
//Note: A leaf is a node with no children.
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type NodeWithDepth struct {
	node  *TreeNode
	depth int
}

//sol1 BFS
func maxDepthBFS(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := make([]NodeWithDepth, 0, 1024)
	q = append(q, NodeWithDepth{root, 1})

	maxDepth := 0
	for len(q) > 0 {
		nd := q[0]
		if nd.depth > maxDepth {
			maxDepth = nd.depth
		}

		if nd.node.Left != nil {
			q = append(q, NodeWithDepth{nd.node.Left, nd.depth + 1})
		}
		if nd.node.Right != nil {
			q = append(q, NodeWithDepth{nd.node.Right, nd.depth + 1})
		}
		q = q[1:]
	}
	return maxDepth

}

func main() {

}

//sol2 DFS
func maxDepthDFS(root *TreeNode) int {
	if root == nil {
		return 0
	}
	md = 1
	if root.Left != nil {
		dfs(root.Left, 2)
	}
	if root.Right != nil {
		dfs(root.Right, 2)
	}
	return md
}

var md int

func dfs(node *TreeNode, depth int) {
	if depth > md {
		md = depth
	}
	if node.Left != nil {
		dfs(node.Left, depth+1)
	}
	if node.Right != nil {
		dfs(node.Right, depth+1)
	}
}
