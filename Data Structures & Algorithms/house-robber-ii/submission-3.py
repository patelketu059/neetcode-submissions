class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1 2 3 4 5] --> [1 2 3 4] and [2 3 4 5] 
        # [1 2 3 4] --> [1 2 3] and [2 3 4]

        # RECURSE
        # def rec(i, arr):
        #     if i >= len(arr): return 0
        #     return max(arr[i] + rec(i + 2, arr), rec(i + 1, arr))

        # return max(rec(0, nums[1:]), rec(0, nums[:-1]))

        # BOTTOM UP
        if len(nums) <= 2: return max(nums)
        dp = [-1] * (len(nums) - 1)
        total = 0

        def rec(i, arr):
            if i >= len(arr): return 0
            if dp[i] != -1: return dp[i]
            dp[i] = max(arr[i] + rec(i + 2, arr), rec(i + 1, arr))
            return dp[i]

        L = rec(0, nums[1:])
        dp = [-1] * (len(nums) - 1)
        R = rec(0, nums[:-1])
        return max(L, R)
        
