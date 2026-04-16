class Solution:
    def findOrder(self, numCourses: int, courses: List[List[int]]) -> List[int]:
        
        # VISITED = 2
        # UNVISITED = 0
        # VISITING = 0
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in courses:
            graph[crs].append(pre)
            indegree[pre] += 1

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        res = []
        final = 0
        while q:
            node = q.popleft()
            res.append(node)
            final += 1
            for c in graph[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        if final != numCourses: return []
        return res[::-1]
