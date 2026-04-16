class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(subset, arr):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 

            if len(subset) > len(nums): return

            for j in range(len(arr)):
                subset.append(arr[j])
                backtrack(subset, arr[:j] + arr[j + 1:])
                subset.pop()


        for i in range(len(nums)):
            backtrack([nums[i]], nums[:i] + nums[i + 1:])

        return res