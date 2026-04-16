class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return 0
        intervals = sorted(intervals)
        prevEnd = intervals[0][1]

        res = 0
        print(intervals)
        for start, end in intervals[1:]:

            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return res