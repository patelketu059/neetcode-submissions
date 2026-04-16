class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Recurse 
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i + 1), nums[i] + dfs(i + 2))

        # return dfs(0)

        # # TOP DOWN 
        # n = len(nums)
        # dp = [-1] * (len(nums) + 2)

        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     return dp[i]

        # return dfs(0)

        # Bottom Up 

        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
