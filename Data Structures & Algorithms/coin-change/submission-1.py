class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # def dfs(amount):
        #     if amount <= 0:
        #         return 0
        #     res = float('inf')
            
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))

        #     return res

        # minCoins = dfs(amount)
        # return minCoins if minCoins != float('inf') else -1

        # Top Down
        # dp = dict()
        # def dfs(amount):

        #     if amount <= 0:
        #         dp[amount] = 0
        #         return 0

        #     if amount in dp: 
        #         return dp[amount]

        #     res = float('inf')
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))

        #     dp[amount] = res
        #     return res


        # minCoins = dfs(amount)
        # return minCoins if minCoins != float('inf') else -1

        # Bottom Up

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # [0 13 13 13 13 13 13 13 13 13]
        # [0 1  2  3  4  5  6  7  8   9]
        # [0 1  2  3  4  1  2  3  4   5] 
        # min(13, 1 + (0)) -> 1
        # min(5, 1) -> 1

        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[-1] if dp[-1] != float('inf') else -1






