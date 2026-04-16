class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        T, D = 0, len(matrix) - 1
        exist = False
        
        while T <= D:
            M = (D - T) // 2 + T

            if matrix[M][0] <= target <= matrix[M][-1]: 
                exist = True
                break
            if target < matrix[M][0]: D = M - 1
            if target > matrix[M][-1]: T = M + 1

        if not exist: return False
        L, R = 0, len(matrix[0]) - 1
        while L <= R:
            mid = (R - L) // 2 + L

            if matrix[M][mid] == target: return True
            elif target < matrix[M][mid]: R = mid - 1
            else: L = mid + 1

        return False
        