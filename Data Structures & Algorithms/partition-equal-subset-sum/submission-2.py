class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target % 2 != 0: return False
        target //= 2
        dp = [0] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]

        # print(dp)
        return dp[-1] if dp[-1] else False