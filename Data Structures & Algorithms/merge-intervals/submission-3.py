class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        res.append(intervals[0])
        intervals = intervals[1:]

        for start, end in intervals:

            temp = res.pop()
            if temp[1] < start:
                res.append(temp)
                res.append([start, end])
            elif temp[0] > end:
                res.append([start, end])
                res.append(temp)
            else:
                res.append([min(temp[0], start), max(temp[1], end)])

        return res 