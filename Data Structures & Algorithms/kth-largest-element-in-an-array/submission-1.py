class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            # print(heap)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]