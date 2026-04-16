class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def recurse(n):
        #     if n <= 0: return 0
        #     if n == 1: return 1
        #     if n == 2: return 2

        #     return recurse(n - 1) + recurse(n - 2)
        # return recurse(n)

        # Top Down
        dp = [-1] * (n + 1)
        def dfs(n):
            if n <= 2: 
                dp[n] = n
                return dp[n]
            if dp[n] != -1: return dp[n]

            dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]
        dfs(n)
        return dp[-1]

        # Bottom Up
        # dp = [0, 1, 2]
        # if n <= 2: return n
        # for i in range(3, n + 1):
        #     dp.append(dp[i - 1] + dp[i - 2])

        # return dp[-1]




