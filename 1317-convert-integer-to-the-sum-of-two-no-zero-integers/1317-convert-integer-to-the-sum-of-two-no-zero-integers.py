class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_nonzero(x: int) -> bool:
            if x == 0:
                return False
            while x:
                if x % 10 == 0:
                    return False
                x = x // 10
            return True
        
        for i in range(n//2, n):
            complement = n - i
            if is_nonzero(complement) and is_nonzero(i):
                return [i, complement]
            