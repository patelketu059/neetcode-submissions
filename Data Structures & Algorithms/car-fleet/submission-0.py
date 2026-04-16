class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        d = [(p,s) for p, s in zip(position, speed)]
        d.sort(reverse = True)
        stack = []

        for p, s in d:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
