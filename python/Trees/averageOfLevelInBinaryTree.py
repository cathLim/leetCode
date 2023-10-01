#https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        
        while q:
            lenQ = len(q)
            average = 0
            for i in range (lenQ):
                node = q.popleft()
                if node:
                    average += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            average = average / lenQ
            res.append(average)
        return res
		