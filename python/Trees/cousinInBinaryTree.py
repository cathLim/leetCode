#https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, None)]) #node, parent

        while q:
            lenQ = len(q)
            x_parent, y_parent = None, None
            for i in range(lenQ):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            if x_parent is not None and y_parent is not None and x_parent != y_parent:
                return True
        return False