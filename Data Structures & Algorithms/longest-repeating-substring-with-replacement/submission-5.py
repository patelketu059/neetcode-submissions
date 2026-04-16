class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        charSet = defaultdict(int)
        maxF = 0
        L = 0
        res = 0
        for R, c in enumerate(s):
            charSet[c] += 1
            maxF = max(maxF, charSet[c])

            while (R - L + 1) - maxF > k:
                charSet[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)

        return res

                    
            

