class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operations = set(['+', '-', '*', '/'])
        for i in tokens:
            print(stack)
            if i in operations:
                second = stack.pop()
                first = stack.pop()

                if i == '+': stack.append(first + second)
                elif i == '-': stack.append(first - second)
                elif i == '*': stack.append(first * second)
                else:
                    if first / second < 0:
                        stack.append(math.ceil(first / second))
                    else:
                        stack.append(math.floor(first / second))
            else:
                
                stack.append(int(i))


        return int(stack[-1])
