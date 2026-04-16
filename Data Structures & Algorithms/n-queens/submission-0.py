class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        col = set()
        posDiag = set() # R + C 
        negDiag = set() # R - C

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board.copy()])
                return 

            for c in range(n):
                if not(c in col or (r + c) in posDiag or (r - c) in negDiag):
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'
                    dfs(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'

        dfs(0)
        return res

