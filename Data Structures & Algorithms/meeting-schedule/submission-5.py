"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1: return True
        sorted(intervals, key = lambda x: x.start)
        interval = intervals[0]
        intervals = intervals[1:]


        for curr in  intervals:
            if interval.end <= curr.start:
                interval = curr
            elif curr.end <= interval.start:
                continue
            else:
                return False

        return True