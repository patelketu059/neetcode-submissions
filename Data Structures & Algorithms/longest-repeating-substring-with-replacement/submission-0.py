class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        L, res, maxC = 0, 0, 0
        freq = defaultdict(int)

        for R in range(len(s)):
            freq[s[R]] += 1
            maxC = max(maxC, freq[s[R]])
            while R - L + 1 - maxC > k:
                freq[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res
