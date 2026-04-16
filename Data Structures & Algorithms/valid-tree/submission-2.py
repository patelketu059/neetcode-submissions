class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 < len(edges): return False
        graph = defaultdict(list)
        VISITED = 2
        UNVISITED = 0
        VISITING = 1
        states = [UNVISITED] * n
        self.finish = 0

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        def dfs(node, parent):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False

            states[node] = VISITING
            for nei in graph[node]:
                if nei == parent: continue
                if not dfs(nei, node):
                    return False
            
            self.finish += 1
            states[node] = VISITED
            return True
        return dfs(0, -1) and self.finish == n


        
