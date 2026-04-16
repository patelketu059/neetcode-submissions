class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def isAlphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or 
               ord('A') <= ord(c) <= ord('Z') or 
               ord('0') <= ord(c) <= ord('9'))

        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not isAlphaNum(s[L]):
                L += 1
            while R > L and not isAlphaNum(s[R]):
                R -= 1

            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True
        

