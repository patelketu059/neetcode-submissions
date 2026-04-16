class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) <= 1: return len(position)
        pos_spd = dict(zip(position, speed))
        pos_spd = sorted(pos_spd.items(), key = lambda x: x[0], reverse = True)
        stack = []
        res = 0
        # print(pos_spd)
        for k, v in pos_spd:
            time =  (target - k) / v 
            # print(k, v, time)

            if stack and  time <= stack[-1]:
                continue
            else:
                stack.append(time)
                res += 1

        return res