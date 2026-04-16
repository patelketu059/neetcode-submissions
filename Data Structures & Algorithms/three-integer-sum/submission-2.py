class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                total = nums[L] + nums[R] + num

                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L -1]:
                        L += 1

        return res