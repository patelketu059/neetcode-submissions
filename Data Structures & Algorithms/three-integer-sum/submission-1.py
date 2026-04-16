class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def twoSum(curr, nums):
            result = set()
            L, R = 0, len(nums) - 1
            while L < R:
                value = curr + nums[L] + nums[R]
                if value == 0: 
                    result.add(tuple([nums[L], nums[R], curr]))
                    L += 1
                if value > 0: R -= 1
                elif value < 0: L += 1
            return result

        for i, num in enumerate(nums):
            temp = twoSum(num, nums[i + 1:])
            if len(temp) > 0:
                for i in temp:
                    res.add(i)
        return list(res)