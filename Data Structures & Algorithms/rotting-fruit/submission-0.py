class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 2:
                    q.append((R, C))
                if grid[R][C] == 1:
                    fresh += 1


        def bfs(r, c, fresh):
            if not (r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or 
                    grid[r][c] != 1):
                q.append((r, c))
                fresh -= 1
                grid[r][c] = 2
            return fresh

        while q and fresh > 0: 
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                for dr, dc in directions:
                    fresh = bfs(dr + r, dc + c, fresh)

            time += 1

        return time if fresh == 0 else -1