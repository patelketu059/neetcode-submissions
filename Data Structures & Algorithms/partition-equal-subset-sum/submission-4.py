class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target % 2 != 0: return False
        target //= 2

        # def dfs(i, target):
        #     if i >= len(nums):
        #         return target == 0

        #     if target < 0: return False

        #     return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        # return dfs(0, sum(nums) // 2)


        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()

            for t in dp:
                if (t + nums[i]) == target: return True
                nextDP.add(t + nums[i])
            dp = nextDP
        return True if target in dp else False
        # dp = {}
        # def dfs(i, target):

        #     if i >= len(nums): return target == 0
        #     if target < 0: return False
        #     if (i, target) in dp: return dp[(i, target)]

        #     dp[(i + 1, target)] = dfs(i + 1, target)
        #     dp[(i + 1, target - nums[i])] = dfs(i + 1, target - nums[i])
        #     dp[(i, target)] = dp[(i + 1, target)] or dp[(i + 1, target - nums[i])]

        #     return dp[(i, target)]
        # return dfs(0, target)

