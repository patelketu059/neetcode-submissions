class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s) - 1

        def alphanum(ch):
            if 'a' <= ch <= 'z' or \
             'A' <= ch <= 'Z' or \
             '0' <= ch <= '9':
                return True

        while L <= R:
            if not alphanum(s[L]):
                L += 1
            elif not alphanum(s[R]):
                R -= 1
            elif s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
                
        return True

