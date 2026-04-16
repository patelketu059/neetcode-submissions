class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDist(point):
            x, y = point[0], point[1]
            return (x**2 + y**2)**0.5

        minHeap = []
        for i in points:
            minHeap.append([calcDist(i), i ])

        res = []
        heapq.heapify(minHeap)
        while k > 0:
            dist, point = heapq.heappop(minHeap)
            res.append(point)
            k -= 1

        return res