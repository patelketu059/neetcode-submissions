class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return 
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        def bfs(r, c):
            if not (r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    (r, c) in visit or grid[r][c] == -1):
                visit.add((r, c))
                q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft() 
                grid[r][c] = dist
                for dr, dc in directions:
                    bfs(dr + r, dc + c)
            dist += 1

        return 