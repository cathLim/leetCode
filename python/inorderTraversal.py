https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#There are two different methods
#Method 1:  using the recursive method, repeat calling itself
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root):
            #this is our base case
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result


#Method 2: using the iteration method, stack -> LIFO to push and pop the values
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []    
        current = root

        #current pointer and stack are not empty
        while current or stack:
            while current:
                stack.append(current)
                current = current.left #move our current pointer down to the left
            #until the current is pointing to the NULL, exit the while loop
            current = stack.pop()
            result.append(current.val)
            #after append it, then shift to the right
            current = current.right
        return result
"""
