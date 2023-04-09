class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0

        out = set()        
        x = 2
        while x ** 2 < n:
            if x not in out:
                for p in range(x ** 2, n, x):
                    out.add(p)
            x += 1
        
        INCLUDING_ITSELF_AND_TWO = 2
        return n - INCLUDING_ITSELF_AND_TWO - len(out)
                
        