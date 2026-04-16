class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # # REcursive
        # def dfs(i, j):
        #     if i == len(nums):
        #         return 0
        #     LIS = dfs(i + 1, j) 
        #     if j == -1 or nums[j] < nums[i]:
        #         LIS = max(LIS, 1 + dfs(i + 1, i))
        #     return LIS
        # return dfs(0, -1)

        # Top Down
        # dp = [-1] * len(nums)
        # def dfs(i):
        #     if i == len(nums):
        #         return 0
        #     if dp[i] != -1: return dp[i]
        #     LIS = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, 1 + dfs(j))
        #     dp[i] = LIS
        #     return LIS
        # dfs(0)
        # return max(dfs(i) for i in range(len(nums)))


        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1 ,-1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                
        return max(LIS)









