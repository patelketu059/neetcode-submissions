class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (R - L) // 2 + L

            if nums[M] == target: return M
            if target > nums[M]: L = M + 1
            else:
                R = M - 1

        return -1 