class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = [newInterval]

        for start, end in intervals:
            temp = res.pop()
            if temp[1] < start:
                res.append(temp)
                res.append([start, end])
            elif end < temp[0]:
                res.append([start, end])
                res.append(temp)
            else:
                res.append([min(start, temp[0]), max(end, temp[1])])
        return res
