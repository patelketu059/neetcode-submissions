class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     res = float('inf')

        #     for c in coins:
        #         if amount - c >= 0:
        #             res = min(res, 1 + dfs(amount - c))
        #     return res
        # res = dfs(amount)
        # return res if res != float('inf') else -1

        # Bottom Up
        dp = [-1] * (amount + 1)
        def dfs(amount):
            if amount == 0: 
                dp[amount] = 0
                return 0

            if dp[amount] != -1: return dp[amount]
            res = float('inf')

            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
                    
            dp[amount] = res
            return res

        res = dfs(amount)
        return res if res != float('inf') else -1
