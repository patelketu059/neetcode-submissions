class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles): return max(piles)

        L, R = 1, max(piles)
        res = -1
        while L <= R:
            M = (R - L) // 2 + L
            count = 0
            for i in piles:
                count += math.ceil(float(i) / M)

            if count <= h:
                res = M
                R = M - 1
            else:
                L = M + 1

        return res 