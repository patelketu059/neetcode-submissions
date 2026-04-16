class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree = [0] * numCourses
        # adj = [[] for _ in range(numCourses)]

        # for crs, pre in prerequisites:
        #     indegree[pre] += 1
        #     adj[crs].append(pre)

        # q = deque()

        # for n in range(numCourses):
        #     if indegree[n] == 0:
        #         q.append(n)

        # finish = 0
        # while q:
        #     node = q.popleft()
        #     finish += 1

        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        # return finish == numCourses


        ## DETECTING CYCLES
        VISITED = 2
        UNVISITED = 0
        VISITING = 1
        graph = defaultdict(list)
        states = [UNVISITED] * numCourses

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False
            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei): return False
            states[node] = VISITED
            return True


        for n in range(numCourses):
            if not dfs(n): return False

        return True





