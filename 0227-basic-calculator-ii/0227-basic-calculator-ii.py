class Solution:
    def calculate(self, s: str) -> int:
        OPS = "+-*/"
        ADD, SUB, MUL, DIV = OPS
        SENTRY = "+0"
        s = s.replace(' ', '') + SENTRY
        
        nums = []
        carry = 0
        op = ADD
        for c in s:
            if c.isnumeric():
                carry = carry * 10 + int(c)
                continue
            if op == ADD:
                nums.append(carry)
            elif op == SUB:
                nums.append(-carry)
            elif op == MUL:
                nums.append(nums.pop() * carry)
            else:
                nums.append(math.trunc(nums.pop() / carry))
            op = c
            carry = 0
        
        return sum(nums)
        