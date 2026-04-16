class Solution:
    def numDecodings(self, s: str) -> int:
        
        # chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # nums = range(1, 28)
        # vals = list(zip(chars, nums))
        # print(vals)

        # def dfs(i):
        #     if i == len(s):
        #         return 1

        #     if s[i] == '0':
        #         return 0
        #     res = dfs(i + 1)
        #     if i < len(s) - 1:
        #         if (s[i] == '1' or
        #             (s[i] == '2' and s[i + 1] < '7')):
        #             res += dfs(i + 2)
        #     return res
        # return dfs(0)

        n = len(s) + 1
        dp = [-1] * n

        def dfs(i):
            if i == len(s):
                dp[i] = 1
                return 1
            
            if s[i] == '0':
                dp[i] = 0
                return 0
            
            if dp[i] != -1: return dp[i]
            if dp[i + 1] != -1:
                res = dp[i + 1]
            else:
                res = dfs(i + 1)

            if i < len(s) - 1:
                if (s[i] == '1' or
                    (s[i] == '2' and s[i + 1] < '7')):
                    if dp[i + 2] != -1:
                        res += dp[i + 2]
                    else: 
                        res += dfs(i + 2)
            return res
        return dfs(0)



