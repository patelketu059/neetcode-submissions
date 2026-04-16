class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        visited = set()

        def twoSum(index):
            target = -nums[index]
            prevMap = {}
            for i in range(index + 1, len(nums)):
                comp = target - nums[i] 
                if comp in prevMap:
                    res.add((nums[index], comp, nums[i]))
                prevMap[nums[i]] = i


        for i in range(len(nums)):
            if i not in visited:
                twoSum(i)
            visited.add(i)

        return list(res)


            