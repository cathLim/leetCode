/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseList(head *ListNode) *ListNode {
    var prev, current *ListNode
	current = head

	for current != nil{
		tmp = current.Next
		current.Next = prev
		prev = current
		current = tmp 
	}
	return prev
 }