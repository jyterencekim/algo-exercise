class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_nonzero(x: int) -> bool:
            return '0' not in str(x)
        
        for i in range(n//2, n):
            complement = n - i
            if is_nonzero(complement) and is_nonzero(i):
                return [i, complement]
            