class Solution:
    def trap(self, height: List[int]) -> int:
        
        # main - [0 2 0 3 1 0 1 3 2 1]
        # left - [0 0 2 0 2 3 2 0 1 2]
        # right- [3 1 3 0 2 3 2 0 0 0]
        # min -  [0 0 2 0 2 3 2 0 0 0 ]

        left = [0]
        right = [0] * len(height)
        leftM = height[0]
        rightM = height[-1]
        length = len(height) - 1

        for i in range(1, len(height)):
            left.append(max(leftM - height[i], 0))
            leftM = max(leftM, height[i])

            right[length - i] = max(0, rightM - height[length - i])
            rightM = max(rightM, height[length - i])

        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i])
        return total