class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # nums = list(set(nums))
        nums.sort()
        res = set()

        def dfs(i, subset):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return 

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return list(res)