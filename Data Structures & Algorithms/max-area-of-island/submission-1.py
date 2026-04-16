class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1):
                return 0
            
            grid[r][c] = 'X'
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for R in range(ROWS):
            for C in range(COLS):
                if grid[R][C] == 1:
                    maxArea = max(maxArea, dfs(R, C))

        return maxArea