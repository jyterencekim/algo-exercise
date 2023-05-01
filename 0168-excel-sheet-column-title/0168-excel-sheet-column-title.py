class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        D = 26
        def to_char(num: int) -> chr:
            return chr(ord('A') - 1 + num)
        
        result = []
        carry = columnNumber
        
        while carry:
            remainder = carry % D
            if not remainder:
                remainder = D
            result.append(to_char(remainder))
            carry -= remainder
            carry //= D
            
        return ''.join(reversed(result))
            
        