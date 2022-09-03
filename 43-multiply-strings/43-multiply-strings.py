class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def to_number(s: str) -> int:
            if not s:
                return 0
            return ord(s[-1]) - ord('0') + 10 * to_number(s[:-1])
        
        return str(to_number(num1) * to_number(num2))