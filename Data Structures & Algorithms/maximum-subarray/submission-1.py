class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = float('-inf')
        runningSum = 0
        for R in nums:
            runningSum += R
            if runningSum < R:
                runningSum = R
            maxSum = max(maxSum, runningSum)

        return maxSum
        