#https://leetcode.com/problems/invert-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #check the base case: root Null, return Null
        if not root:
            return None

        #otherwise, swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #make a recursive call for both left and right root
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


        
        