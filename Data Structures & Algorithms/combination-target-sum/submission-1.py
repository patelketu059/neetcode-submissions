class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset, total):
            if total > target or i >= len(nums): return
            if total == target: 
                res.append(subset.copy())
                return 

            # total += nums[i]
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            dfs(i + 1, subset, total)


        dfs(0, [], 0)
        return res
            

        