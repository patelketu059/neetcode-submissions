class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        maxC = 0
        L = 0
        store = set()

        for R in range(len(s)):

            if s[R] in store:
                while L < R and s[R] in store:
                    store.remove(s[L])
                    L += 1
            maxC = max(maxC, R - L + 1)
            store.add(s[R])

        return maxC


