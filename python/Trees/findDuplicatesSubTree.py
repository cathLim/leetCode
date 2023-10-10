#https://leetcode.com/problems/find-duplicate-subtrees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)

        def preOrder(node):
            if not node:
                return "null"
            left_str = preOrder(node.left)
            right_str = preOrder(node.right)
            s = ",".join([str(node.val), left_str, right_str])
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        res = []
        if root:
            preOrder(root)
        return res