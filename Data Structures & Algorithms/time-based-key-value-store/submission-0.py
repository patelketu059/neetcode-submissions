class TimeMap:

    def __init__(self):
        self.timeKey = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeKey[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeKey[key]
        L, R = 0, len(arr) - 1
        res = ""
        while L <= R:
            M = L + (R - L) // 2
            if arr[M][0] == timestamp:
                return arr[M][1]
            if timestamp < arr[M][0]:
                R = M - 1
            else:
                res = arr[M][1]
                L = M + 1
        return res

        
