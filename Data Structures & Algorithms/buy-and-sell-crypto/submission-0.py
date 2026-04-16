class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        prev = prices[0]
        for R in prices:
            prev = min(prev, R) 
            maxP = max(maxP, R - prev)

        return maxP