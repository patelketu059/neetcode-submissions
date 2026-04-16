class Solution:
    def trap(self, height: List[int]) -> int:
        LEFT = [0] * len(height)
        maxL, maxR = height[0], height[-1]
        count = 0
        for ind in range(len(height)):
            if maxL <= height[ind]:
                maxL = height[ind]
            else:
                LEFT[ind] = maxL - height[ind]

        
        for ind in range(len(height) - 1, -1, -1):
            if maxR <= height[ind]:
                maxR = height[ind]
            else:
                count += min(LEFT[ind], maxR - height[ind])

        return count 