class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxVal, minVal = 1,1
        res = nums[0]

        for num in nums:
            temp = maxVal
            maxVal = max(maxVal * num, num, minVal * num)
            minVal = min(minVal * num, num, temp * num)
            res = max(res, maxVal, minVal)

        return res




