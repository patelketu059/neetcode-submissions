class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i):

            if i == len(nums):
                res.append(nums.copy())
                return

            for k in range(i, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                backtrack(i + 1)
                nums[i], nums[k] = nums[k], nums[i]

        backtrack(0)
        return res