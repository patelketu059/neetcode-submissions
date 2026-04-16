class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:

            if nums[L] <= nums[R]:
                return nums[L]

            M = L + (R - L) // 2
                        
            if nums[M] > nums[R]:
                L = M + 1
            else: # M < R
                R = M 

        