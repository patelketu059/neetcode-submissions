class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        target = len(nums) - 1
        

        for n in range(len(nums) - 2, -1, -1):
            if nums[n] + n >= target:
                target = n
            
        return target == 0