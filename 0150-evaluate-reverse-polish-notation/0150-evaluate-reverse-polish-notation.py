class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = "+-*/"
        ADD, SUBTRACT, MULTIPLY, DIVIDE = OPERATORS
        
        
        for token in tokens:
            if token not in OPERATORS:
                stack.append(int(token))
            else:
                # assuming only correct notations
                b, a = stack.pop(), stack.pop()
                result = None
                if token == ADD:
                    result = a + b
                elif token == SUBTRACT:
                    result = a - b
                elif token == MULTIPLY:
                    result = a * b
                else:
                    result = int(a / b)
                stack.append(result)
        
        return stack[-1]
                    