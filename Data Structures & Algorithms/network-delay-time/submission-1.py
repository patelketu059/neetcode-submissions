class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = dict()
        time = []
        
        def dfs(k, t):
            if k in visited and visited[k] < t:
                visited[k] = min(visited[k], t)
                return 0

            visited[k] = t
            
            for i in times:
                if i[0] == k:
                    dfs(i[1], t + i[2])

        dfs(k, 0)
        print(visited)
        if len(visited) == n: return max(visited.values())
        return -1

