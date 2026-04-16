class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Recurse 
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # return min(dfs(0), dfs(1))


        # Top Down 

        dp = [0] * (len(cost) + 2)
        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i + 1] == 0:
                one = dp[i + 1] if dp[i + 1] != 0 else dfs(i + 1)

            if dp[i + 2] == 0:
                two = dp[i + 2] if dp[i + 2] != 0 else dfs(i + 2)

            return cost[i] + min(one, two)

        return min(dfs(0), dfs(1))