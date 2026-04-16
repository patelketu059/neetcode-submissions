class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def recurse(n):
        #     if n <= 0: return 0
        #     if n == 1: return 1
        #     if n == 2: return 2

        #     return recurse(n - 1) + recurse(n - 2)
        # return recurse(n)

        dp = [0, 1, 2]
        if n <= 2: return n
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]