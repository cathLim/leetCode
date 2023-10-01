"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""
def findSuccessor(root):
	q = deque([root])
	res = []
	
    if not root:
        return NONE
	
	while q:
		node = q.popleft()
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
		if node.val == key:
			break
    return q.popleft()
		