class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        if len(nums) == 1: 
            if nums[0] == target: return 0
            else: 
                return -1


        while L < R:

            M = (R - L) // 2 + L
            if nums[L] < nums[R]: 
                break
            else:
                if nums[M] > nums[R]: 
                    L = M + 1
                else: # M < R
                    R = M

        # print(L, nums[L])
        break_point = L
        L, R = 0, len(nums) - 1
        if target >= nums[break_point] and target <= nums[R]:
            L = break_point
        else:
            R = break_point - 1

        while L <= R:
            # print("L: ", nums[L])
            M = (R - L) // 2 + L
            # print("M: ", nums[M])
            if nums[M] == target:
                return M
            elif target > nums[M]:
                L = M + 1
            else:
                R = M - 1

        return -1