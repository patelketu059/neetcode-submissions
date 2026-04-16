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

        # Top Down
        # dp = [-1] * (amount + 1)
        # def dfs(amount):
        #     if amount == 0: 
        #         dp[amount] = 0
        #         return 0

        #     if dp[amount] != -1: return dp[amount]
        #     res = float('inf')

        #     for c in coins:
        #         if amount - c >= 0:
        #             res = min(res, 1 + dfs(amount - c))
                    
        #     dp[amount] = res
        #     return res

        # res = dfs(amount)
        # return res if res != float('inf') else -1

        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[-1] if dp[-1] != amount + 1 else -1
        # [12 12 12 12 12 12 12 12 12 12 12 12 12]
        # [0   1  2  3  4  5  6  7  8  9 10 11 12]    


