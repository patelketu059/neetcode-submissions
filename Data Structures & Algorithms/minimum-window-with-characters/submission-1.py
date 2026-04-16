class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 1. s == t
        if s == t: return t

        # 2. len(s) > len(t)
        if len(s) < len(t): return ""

        # 2. Shrink Left and Right if not part of t
        L, R = 0, len(s) - 1
        while L < len(s) and s[L] not in t:
            L += 1
        
        while R > L and s[R] not in t:
            R -= 1

        s = s[L:R+1]
        if len(s) < len(t): return ""


        t_c = Counter(t)
        # print("T_C: ", t_c)

        window = defaultdict(int)
        res, resLen = [-1, -1], float('inf')
        L = 0


        required = len(t_c)
        formed = 0


        for R in range(len(s)):
            c = s[R]
            window[c] += 1

            if c in t_c and window[c] == t_c[c]:
                formed += 1

            while formed == required:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R - L + 1

                window[s[L]] -= 1
                if s[L] in t_c and window[s[L]] < t_c[s[L]]:
                    formed -= 1
                
                L += 1
        
        L, R = res
        # print(res, resLen)/
        return s[L: R + 1] if resLen != float('inf') else ""
                





        
