class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = Counter(nums)
        res = []
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp != nums[i] and comp in count:
                res.append(i)
                break
            elif comp == nums[i] and count[comp] > 1:
                res.append(i)
                break
            
        

        for j in range(res[-1] + 1, len(nums)):
            if comp == nums[j]:
                res.append(j)
                return res
            

        
        

        