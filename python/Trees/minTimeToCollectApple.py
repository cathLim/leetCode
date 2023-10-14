#https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        def dfs(node, parent):
            time = 0
            for child in adj[node]:
                if child != parent:
                    time += dfs(child, node)
            if (time or hasApple[node]) and node != 0:
                time += 2
            return time
        return dfs(0, None)