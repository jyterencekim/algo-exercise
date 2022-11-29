class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        
        divs = Counter()
        target = num
        for divisor in range(9, 1, -1):
            while target % divisor == 0:
                target //= divisor
                divs[divisor] += 1
        
        if target != 1:
            return 0
        
        digits = []
        for d, c in divs.items():
            if c:
                digits.extend([d] * c)
        digits.sort()
        
        result = int(''.join(str(d) for d in digits))
        
        return result if result < 2 ** 31 else 0
        
         