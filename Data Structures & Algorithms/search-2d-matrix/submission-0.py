class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        Row = -1
        while L <= R:
            M = L + (R - L) // 2
            if matrix[M][0] <= target <= matrix[M][-1]:
                Row = M
                break
            if target < matrix[M][0]:
                R = M - 1
            else:
                L = M + 1

        L, R = 0, len(matrix[0]) - 1
        if Row == -1: return False

        while L <= R:
            M = L + (R - L) // 2
            if matrix[Row][M] == target: return True
            if target < matrix[Row][M]: R = M - 1
            else: L = M + 1

        return False