class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n <= 1:
            return n
        
        return math.floor(math.sqrt(n))