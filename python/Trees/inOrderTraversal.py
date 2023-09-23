#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Iterative approach
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []    
        current = root

        #current pointer and stack are not empty
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result