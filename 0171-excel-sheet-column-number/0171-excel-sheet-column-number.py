class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def to_number(c: chr) -> int:
            return ord(c) - ord('A') + 1
        D = len(string.ascii_uppercase) # 26
        
        result = 0
        for c in columnTitle:
            result *= D
            result += to_number(c)
        
        return result
        
        