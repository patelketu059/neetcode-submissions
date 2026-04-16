class Solution:
    def jump(self, nums: List[int]) -> int:
        
        L, R = 0, 0
        res = 0
        while R < len(nums) - 1:
            far = 0
            for i in range(L, R + 1):
                far = max(far, nums[i] + i)

            L = R + 1
            R = far
            res += 1

        return res
