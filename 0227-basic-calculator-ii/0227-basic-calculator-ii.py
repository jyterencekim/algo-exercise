class Solution:
    def calculate(self, s: str) -> int:
        OPS = "+-*/"
        ADD, SUB, MUL, DIV = OPS
        
        s = s.replace(' ', '')
        
        # base
        exp = ['+']
        
        def read_number(pt: int, s: str) -> Tuple[int]:
            c = []
            while pt < len(s) and s[pt].isnumeric():
                c.append(s[pt])
                pt += 1
            number = int(''.join(c)) if c else None
            return number, pt
        
        pt = 0
        while pt < len(s):
            curr, pt = read_number(pt, s)
            if exp[-1] == MUL:
                exp.pop()
                prev = exp.pop()
                exp.append(math.floor(prev * curr))
            elif exp[-1] == DIV:
                exp.pop()
                prev = exp.pop()
                exp.append(math.floor(prev / curr))
            else:
                if curr is not None:
                    exp.append(curr)
                else: 
                    exp.append(s[pt])
            
            if curr is None:
                pt += 1
        
        result = 0
        for i, curr in enumerate(exp):
            if curr in (ADD, SUB):
                continue
            if exp[i - 1] == ADD:
                result += curr
            elif exp[i - 1] == SUB:
                result -= curr
                
        return int(math.floor(result))
        