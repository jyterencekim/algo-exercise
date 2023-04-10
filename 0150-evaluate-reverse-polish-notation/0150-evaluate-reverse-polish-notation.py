class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = "+-*/"
        ADD, SUBTRACT, MULTIPLY, DIVIDE = OPERATORS
        
        def is_number(x: str) -> bool:
            # assuming one char operators only
            return x.isnumeric() or (len(x) > 1 and x[1].isnumeric())
        
        
        for token in tokens:
            if is_number(token):
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
                    