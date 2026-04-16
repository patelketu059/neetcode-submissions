class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = Counter(nums)
        res = []
        for curr in range(len(nums)):
            comp = target - nums[curr]
            if freq[comp]:
                if comp == nums[curr]:
                    if freq[comp] > 1: 
                        res.append(curr)
                        break
                    else:
                        continue
                else:
                    res.append(curr)
                    break


        for i in range(curr + 1, len(nums)):
            if nums[i] == comp:
                res.append(i)
                break
 

        return res 

