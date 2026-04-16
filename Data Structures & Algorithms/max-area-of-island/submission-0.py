class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0


        def bfs(r, c, area):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            
            while q:
                r, c = q.popleft()
                for dr, dc in direction:
                    nr, nc = dr + r, dc + c
                    if not (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] == 0):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c, 1))

        return res
                