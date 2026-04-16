class Solution:
    def longestPalindrome(self, s: str) -> str:
        
                
        # if len(s) <= 2:
        #     return s[0]
        

        res = 0
        resInd = 0
        for i in range(0, len(s)):
            
            # IF ODD 
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if res < (R - L + 1):
                    resInd = L
                    res = R - L + 1
                L -= 1
                R += 1

            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if res < (R - L + 1):
                    resInd = L
                    res = R - L + 1
                L -= 1
                R += 1
        
        return s[resInd: resInd + res]