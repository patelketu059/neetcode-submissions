class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1   1 2 8]
        # [48 24 6 1]
        # [48 24 12 8]

        # [1 -1 0 0 0]
        # [0  6 6 3 1]
        # [0 -6 0 0 0]

        preSum = [1]
        postSum = [1] * len(nums)

        for i in range(1, len(nums)):
            # print(i , len(nums) - i - 1)
            index = len(nums) - i - 1
            preSum.append(preSum[-1] * nums[i - 1])
            postSum[index] = postSum[index + 1] * nums[index + 1]

        # print(preSum)
        # print(postSum)
        return [preSum[i] * postSum[i] for i in range(len(nums))]
