class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L, R = 0, len(numbers) - 1
        while L < R:
            curr = numbers[L] + numbers[R]
            if curr == target: return [L + 1, R + 1]
            if curr < target: L += 1
            elif curr > target: R -= 1
            