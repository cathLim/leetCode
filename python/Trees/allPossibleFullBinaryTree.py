# https://leetcode.com/problems/all-possible-full-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = { 0 : [], 1 : [ TreeNode() ] }

        # return the list of full binary tree within n nodes
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n): # 0 - (n-1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res
        
        return backtrack(n)
