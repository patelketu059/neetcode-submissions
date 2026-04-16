class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(point):
            x, y = point
            return (x**2 + y**2)**(0.5)

        minHeap = []
        for point in points:
            heapq.heappush(minHeap, (dist(point), point))

        return [heapq.heappop(minHeap)[1] for _ in range(k)]

