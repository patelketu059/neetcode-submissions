class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for M in range(len(s)):
            L, R = M, M

            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1

            L, R = M, M + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1

        return res
