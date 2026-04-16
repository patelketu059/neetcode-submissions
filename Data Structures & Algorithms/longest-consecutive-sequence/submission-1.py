class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
    
        res = 0
        vals = set(nums)

        for v in vals:
            if (v - 1) not in vals:
                count = 1
                while (v + count) in vals:
                    count += 1
                res = max(res, count)
            
        return res