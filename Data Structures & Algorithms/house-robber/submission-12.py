class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Recursion

        # def dfs(i):
        #     if i >= len(nums): return 0
        #     return max(nums[i] + dfs(i + 2), dfs(i + 1))


        # return max(dfs(0), dfs(1))

        # Top Down
        dp = [-1] * len(nums) 

        def dfs(i):
            if i >= len(nums): return 0
            if dp[i] != -1: return dp[i]

            dp[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return dp[i]

        dfs(0)
        return dp[0]

