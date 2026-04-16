"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node: return None
        # new = {}

        # def dfs(node):
        #     if node in new: return new[node]

        #     copy = Node(node.val)
        #     new[node] = copy
        #     for n in node.neighbors:
        #         copy.neighbors.append(dfs(n))

        #     return copy

        # return dfs(node) 

        if not node: return None
        graph = {}
        graph[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in graph:
                    graph[n] = Node(n.val)
                    q.append(n)
                graph[curr].neighbors.append(graph[n])

        return graph[node]
