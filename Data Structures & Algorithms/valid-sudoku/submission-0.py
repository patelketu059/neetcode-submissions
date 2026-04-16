class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        COLS = defaultdict(set)
        ROWS = defaultdict(set)
        Squares = defaultdict(set)

        for R in range(0, 9):
            for C in range(0, 9):
                if board[R][C] == '.':
                    continue
                else:
                    val = board[R][C]
                    if (val in ROWS[R] or 
                        val in COLS[C] or 
                        val in Squares[(R // 3, C // 3)]):
                        return False
                    ROWS[R].add(board[R][C])
                    COLS[C].add(board[R][C])
                    Squares[(R // 3, C // 3)].add(board[R][C])


        return True  

