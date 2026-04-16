class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        BOX = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if (board[r][c] in ROWS[r] or board[r][c] in COLS[c] or 
                    board[r][c] in BOX[(r // 3, c // 3)]):
                    return False
                
                if board[r][c] != '.':
                    ROWS[r].add(board[r][c]) 
                    COLS[c].add(board[r][c])
                    BOX[(r // 3, c // 3)].add(board[r][c])
        return True
            
