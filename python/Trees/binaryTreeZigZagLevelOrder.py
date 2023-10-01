# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        reverse = False

        while q:
            lenQ = len(q)
            level = []

            for i in range(lenQ):
                if not reverse:
                    node = q.popleft()
                    if not node:
                        continue
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    node = q.pop()
                    if not node:
                        continue
                    level.append(node.val)
                    q.appendleft(node.right)
                    q.appendleft(node.left)

            if level:
                res.append(level)
            reverse = not reverse

        return res