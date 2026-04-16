class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        newInterval = intervals[0]
        intervals = intervals[1:]

        for i in intervals:
            if newInterval[1] < i[0]: 
                res.append(newInterval)
                newInterval = i
            elif newInterval[0] > i[1]:
                res.append(i)
            else:
                newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]

        res.append(newInterval)
        return res