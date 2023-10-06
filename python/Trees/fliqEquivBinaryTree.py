#https://leetcode.com/problems/flip-equivalent-binary-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def checkRoot(root1, root2):
            #check if both root are empty
            if not root1 and not root2:
                return True
            
            #check if both root are not equal or one of them is empty
            if not root1 or not root2 or root1.val != root2.val:
                return False
            
            x = (checkRoot(root1.left, root2.left) and checkRoot(root1.right, root2.right))
            y = (checkRoot(root1.left, root2.right) and checkRoot(root1.right, root2.left))

            return x or y

        return checkRoot(root1, root2)