class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        arr = []

        for key, v in count.items():
            heapq.heappush(arr, (v, key))
            if len(arr) > k:
                heapq.heappop(arr)
        
        return [heapq.heappop(arr)[1] for _ in range(k)]