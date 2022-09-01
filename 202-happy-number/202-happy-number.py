class Solution:
    def isHappy(self, n: int) -> bool:
        def digits(x: int) -> int:
            if not x:
                return 0
            while x:
                yield x % 10
                x = x // 10
        seen = set()
        
        while n:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sum(digit ** 2 for digit in digits(n))
        
        return False
            