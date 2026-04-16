class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)]

        for num, cnt in freq.items():
            count[cnt].append(num)

        res = []
        for c in range(len(count) - 1, 0, -1):
            for num in count[c]:
                res.append(num)
                if len(res) == k:
                    return res