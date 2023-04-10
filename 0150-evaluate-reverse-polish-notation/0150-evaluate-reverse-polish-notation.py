class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ADD, SUBTRACT, MULTIPLY, DIVIDE = "+-*/"
        
        def is_number(x: str) -> bool:
            # assuming one char operators only
            return x.isnumeric() or (len(x) > 1 and x[1:].isnumeric())
        
        def to_number(x: str) -> int:
            # assuming ints of valid forms only
            if not x[0].isnumeric():
                return -1 * int(x[1:])
            return int(x)
        
        for token in tokens:
            if is_number(token):
                stack.append(to_number(token))
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
                    is_negative = a * b < 0
                    result = a // b if not is_negative else -(abs(a) // abs(b))
                stack.append(result)
        
        return stack[-1]
                    