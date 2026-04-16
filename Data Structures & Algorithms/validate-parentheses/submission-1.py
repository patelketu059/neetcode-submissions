class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(',
             '}': '{',
             ']': '['}
        
        stack = []

        for i in s:
            if i in d and len(stack) > 0:
                par = stack.pop()
                if par != d[i]: return False
            else:
                stack.append(i)

        return True if len(stack) == 0 else False
        
        