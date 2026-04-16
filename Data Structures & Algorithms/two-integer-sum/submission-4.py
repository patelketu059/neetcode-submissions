class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        prevMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in prevMap:
                return [prevMap[comp], i]
            
            prevMap[nums[i]] = i
        

        
        

        