/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//There are two different methods
//Method 1:  using the recursive method, repeat calling itself
 func inorder(root *TreeNode, result *[] int){
	if root == nil{
		return
	}
	inorder(root.left, result)
	*result = append(*result, root.Val)
	inorder(root.right, result)
 }
 func inorderTraversal(root *TreeNode) []int {
	var result [] int
	inorder(root, &result)
	return result
 }

/*
//Method 2: using the iteration method, stack -> LIFO to push and pop the values
func inorderTraversal(root *TreeNode) []int {
	var result []int
	var s []*TreeNode
	current := root

	for current != nil || len(s) > 0 {
		for current != nil {
			s = append(s, current)
			current = current.Left
		}

		current = s[len(s)-1] // Access the element at the top of the stack
		// this creates a new slice which includess all elements of the original slice (exclude the last one) 
		s = s[:len(s)-1]       // Remove the element from the stack
		result = append(result, current.Val)
		
		current = current.Right
	}
	return result
}




*/