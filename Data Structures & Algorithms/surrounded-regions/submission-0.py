class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(board), len(board[0])


        def dfs(r, c):
            if not (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != 'O'):
                board[r][c] = '#'
                for dr, dc in directions:
                    dfs(dr + r, dc + c)

        for R in range(ROWS):
            if board[R][0] == 'O': dfs(R, 0)
            if board[R][COLS - 1] == 'O': dfs(R, COLS - 1)

        for C in range(COLS):
            if board[0][C] == 'O': dfs(0, C)
            if board[ROWS - 1][C] == 'O': dfs(ROWS - 1, C)


        for R in range(ROWS):
            for C in range(COLS):
                if board[R][C] == '#':
                    board[R][C] = 'O'
                elif board[R][C] == 'O':
                    board[R][C] = 'X'