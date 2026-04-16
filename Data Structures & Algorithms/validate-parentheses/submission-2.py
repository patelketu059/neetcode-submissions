class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        paranthesis = { '}' : '{',
                        ')' : '(',
                        ']' : '['
        }


        for i in s:
            if i not in paranthesis:
                stack.append(i)
            else:
                if len(stack) == 0: return False
                if stack.pop() != paranthesis[i]: return False

        return True if len(stack) == 0 else False 