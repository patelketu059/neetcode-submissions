class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sizeMap = {}
        for index, i in enumerate(intervals):
            sizeMap[tuple(i)] = (i[1] - i[0] + 1)
        sizeMap = sorted(sizeMap.items(), key = lambda x: x[1])
        resMap = {}
        res = []
        seen = set()
        for key, value in sizeMap:
            for i in range(key[0], key[1] + 1):
                if i not in seen:
                    resMap[i] = value
            seen.update(list(range(key[0], key[1] + 1)))

        for q in queries:
            if q not in seen: 
                res.append(-1)
                continue
            res.append(resMap[q])
        return res