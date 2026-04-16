class Solution:
    def trap(self, height: List[int]) -> int:
        
        # main - [0 2 0 3 1 0 1 3 2 1]
        # left - [0 0 2 0 2 3 2 0 1 2]
        # right- [3 1 3 0 2 3 2 0 0 0]
        # min -  [0 0 2 0 2 3 2 0 0 0 ]

        L, R = 0, len(height) - 1
        left, right = height[0], height[-1]
        water = 0

        while L < R:

            if left < right:
                L += 1
                left = max(left, height[L])
                water += left - height[L]
            else:
                R -= 1
                right = max(right, height[R])
                water += right - height[R]

        return water
