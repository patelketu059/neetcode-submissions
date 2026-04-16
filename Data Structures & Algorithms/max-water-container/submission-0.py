class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        area = 0

        while L < R:
            curr = min(heights[R], heights[L]) * (R - L)
            area = max(curr, area)

            if heights[L] > heights[R]: R -= 1
            else:
                L += 1

        return area 