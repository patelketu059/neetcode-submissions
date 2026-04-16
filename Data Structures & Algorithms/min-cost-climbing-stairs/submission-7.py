class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # def dfs(i):
        #     if i >= len(cost): return 0
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))
        
        # return min(dfs(0), dfs(1))


        # TOP DOWN
        # dp = [-1] * len(cost)
        # def dfs(i):
        #     if i >= len(cost): return 0
        #     if dp[i] != -1: return dp[i]

        #     dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

        #     return dp[i]
        
        # return min(dfs(0), dfs(1))

        # Bottom Up
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], 
                        dp[i - 2] + cost[i - 2])

        return dp[-1]
