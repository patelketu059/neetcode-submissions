class Solution:
    def numDecodings(self, s: str) -> int:

        # # REcursive
        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0': return 0
        #     res = dfs(i + 1)
        #     if i < len(s) - 1:
        #         if s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456"):
        #                 res += dfs(i + 2)
        #     return res

        # return dfs(0)
        # Top DOWN
        dp = [-1] * (len(s) + 1)
        def dfs(i):
            if i == len(s):
                dp[i] = 1
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456"):
                    res += dfs(i + 2)
            dp[i] = res
            return res
            
        return dfs(0)
            
