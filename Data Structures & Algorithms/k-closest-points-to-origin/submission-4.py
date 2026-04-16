class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(point):
            x, y = point
            return -(x**2 + y**2)

        maxHeap = []
        for point in points:
            heapq.heappush(maxHeap, (dist(point), point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [heapq.heappop(maxHeap)[1] for _ in range(k)]

