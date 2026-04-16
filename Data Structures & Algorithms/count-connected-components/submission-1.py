class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        visited = set()

        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)


        return res


