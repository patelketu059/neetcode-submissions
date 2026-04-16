class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Recurse

        # if len(nums) < 3:
        #     return max(nums)
        # A = nums[:-1]
        # B = nums[1:]
        # n = len(nums) - 1
        # def dfs(i, arr):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i + 1, arr), arr[i] + dfs(i + 2, arr))
        # return max(dfs(0, A), dfs(0, B))

        # Top Down

        if len(nums) < 3:
            return max(nums)
        # A = nums[:-1]
        # B = nums[1:]
        n = len(nums) - 1

        dp = [-1] * n
        def dfs(i, arr):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i + 1, arr), arr[i] + dfs(i + 2, arr))
            return dp[i]

        dfs(0, nums[:-1])
        A = dp[0]
        dp = [-1] * n
        dfs(0, nums[1:])
        return max(A, dp[0])

