class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()


        def bfs(R, C):
            if (R < 0 or R >= ROWS or 
                C < 0 or C >= COLS or 
                grid[R][C] == -1 or (R, C) in visit):
                return 

            visit.add((R, C))
            q.append([R, C])


        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 0:
                    q.append([R, C])
                    visit.add((R, C))
        
        dist = 0
        while q:
            for i in range(len(q)):
                R, C = q.popleft()
                grid[R][C] = dist
                for dr, dc in directions:
                    bfs(dr + R, dc + C)
            dist += 1

        # return grid