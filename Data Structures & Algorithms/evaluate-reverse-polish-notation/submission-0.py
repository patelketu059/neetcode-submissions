class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 1: return int(tokens[0])

        stack = []
        for val in tokens:
            if val == '+': stack.append(stack.pop() + stack.pop())
            elif val == '-': 
                b = stack.pop()
                a = stack.pop()
                stack.append(a- b)
            elif val == '*': stack.append(stack.pop() * stack.pop())
            elif val == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(math.trunc(a / b) )
            else:
                stack.append(int(val))

        return stack[-1]