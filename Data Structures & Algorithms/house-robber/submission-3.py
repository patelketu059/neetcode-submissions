class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Recurse 
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i + 1), nums[i] + dfs(i + 2))

        # return dfs(0)

        # TOP DOWN 
        n = len(nums)
        dp = [-1] * (len(nums) + 2)

        def dfs(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            nextH = dp[i + 1] if dp[i + 1] != -1 else dfs(i + 1)
            curr = nums[i] + dp[i + 2] if dp[i + 2] != -1 else nums[i] + dfs(i + 2)

            dp[i] = max(nextH, curr)
            return dp[i]

        return dfs(0)