class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) + 1
        indegree = [0] * (n)
        graph = defaultdict(list)
        
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
            indegree[src] += 1
            indegree[des] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        while q:
            node = q.popleft()
            indegree[node] -= 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        for src, des in reversed(edges):
            if indegree[src] == 2 and indegree[des] == 2:
                return [src, des]


    