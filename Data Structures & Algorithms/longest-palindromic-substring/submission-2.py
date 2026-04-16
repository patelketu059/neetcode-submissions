class Solution:
    def longestPalindrome(self, s: str) -> str:
        
                
        # if len(s) <= 2:
        #     return s[0]
        
        # L, R = 0, 0
        # maxC = 0

        # for a in range(0, len(s)):
        #     for b in range(a, len(s)):
        #         # print(s[a:b], s[a:b][::-1])

        #         if s[a:b] == s[a:b][::-1] and len(s[a:b]) > maxC:
        #             maxC = max(maxC, len(s[a:b]))
        #             print("!", s[a:b], True)

        maxC = 0
        index = 0

        for M in range(0, len(s)):
            L, R = M, M
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if maxC < R - L + 1:
                    index = L
                    maxC = R - L + 1
                L -= 1
                R += 1

            L, R = M, M + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if maxC < R - L + 1:
                    index = L
                    maxC = R - L + 1
                L -= 1
                R += 1
            

            
        return s[index : index + maxC]

