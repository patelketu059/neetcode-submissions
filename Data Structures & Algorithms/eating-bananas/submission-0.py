class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            M = L + (R - L) // 2
            time = sum([math.ceil(float(p) / M) for p in piles])

            if time > h:
                L = M + 1
            else:
                res = M
                R = M - 1
        return res