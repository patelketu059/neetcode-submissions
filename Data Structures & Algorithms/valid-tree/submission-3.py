class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 < len(edges): return False
        graph = defaultdict(list)
        VISITED, UNVISITED, VISITING = 2, 0, 1
        states = [UNVISITED] * n

        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
        self.finish = 0

        def dfs(node, parent):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False
            states[node] = VISITING

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node): return False

            states[node] = VISITED
            self.finish += 1
            return True
        dfs(0, -1)
        if self.finish == n: return True
        return False


