class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        seen = set()

        def check(n):
            total = 0
            for i in str(n):
                total += int(i)**2
            return total

        res = n
        while True:
            res = check(res)
            if res == 1:
                return True
            if res in seen:
                return False

            seen.add(res)

