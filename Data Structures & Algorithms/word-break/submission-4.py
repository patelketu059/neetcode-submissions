class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        # def dfs(i):
        #     if i >= len(s):
        #         return True

        #     for word in wordDict:
        #         if ((i + len(word)) <= len(s) and s[i: i + len(word)] == word):
        #             if dfs(i + len(word)):
        #                 return True
        #     return False

        # return dfs(0)

        dp = {len(s) : True}
        def dfs(i):
            if i in dp:
                return dp[i]

            for word in wordDict:
                if ((i + len(word) <= len(s)) and word == s[i: i + len(word)]):
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True

            dp[i] = False
            return False
        
        # dfs(0)
        return dfs(0)








       

        
