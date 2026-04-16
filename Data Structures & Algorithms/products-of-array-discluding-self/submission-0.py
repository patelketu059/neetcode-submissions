class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            pre[i] *= prefix
            prefix *= nums[i]

        pos = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] *= pos
            pos *= nums[i]

        return pre