class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        running = 0
        for R in range(len(nums)):
            
            running += nums[R]
            if running < nums[R]:
                running = nums[R]
            maxSum = max(maxSum, running)
        return maxSum