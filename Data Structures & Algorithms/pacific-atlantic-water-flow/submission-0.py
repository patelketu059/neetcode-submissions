class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [[1,0], [-1, 0], [0, -1], [0, 1]]
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, valid, prev):
            if not (r < 0 or r >= ROWS or 
                    c < 0 or c >= COLS or 
                    (r, c) in valid or heights[r][c] < prev):
                valid.add((r, c))
                for dr, dc in direction:
                    dfs(dr + r, dc + c, valid, heights[r][c])

        for R in range(ROWS):
            dfs(R, 0, pac, heights[R][0])
            dfs(R, COLS - 1, atl, heights[R][COLS - 1])

        for C in range(COLS):
            dfs(0, C, pac, heights[0][C])
            dfs(ROWS - 1, C, atl, heights[ROWS - 1][C])


        for R in range(ROWS):
            for C in range(COLS):
                if (R, C) in pac and (R, C) in atl:
                    res.append([R, C])


        return res