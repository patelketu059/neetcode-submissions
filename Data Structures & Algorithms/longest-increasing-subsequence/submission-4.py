class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        # LIS  = [1] * len(nums)
        # maxC = 0
        # for i in range(1, len(nums)):
        #     for j in range(i, -1, -1):
        #         if nums[i] > nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])

        # return max(LIS)


        arr = [nums[0]]
        nums = nums[1:]
        for num in nums:
            print(arr, num)
            if num > arr[-1]:
                arr.append(num)
            else:
                i = len(arr) - 1
                while i >= 0 and arr[i] >= num:
                    i -= 1
                arr[i + 1] = num

        # print(arr)
        return len(arr)

        # [0,1,0,3,2,3]
        # 0
        # 0 1
        # 0 1
        # 0 1 3
        # 0 1 2
        # 0 1 2 3







