class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        maxHeap = [-s for s in freq.values()]
        heapq.heapify(maxHeap) 
        q = deque()
        time = 0

        while q or maxHeap:
            time += 1
            if maxHeap:
                # time += 1
                curr = 1 + heapq.heappop(maxHeap)
                if curr < 0:
                    q.append((curr, time + n))

            if q and q[0][1] == time:
                v = q.popleft()
                heapq.heappush(maxHeap, v[0])

        return time



