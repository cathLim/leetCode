https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head 

        while current :
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev