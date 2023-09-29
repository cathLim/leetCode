# https://leetcode.com/problems/count-complete-tree-nodes/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time Complexity: O(n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)




