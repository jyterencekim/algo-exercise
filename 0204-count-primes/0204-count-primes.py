class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        candidates = {x for x in range(2, n)}
        
        for x in range(2, n):
            if x not in candidates:
                continue
            if x ** 2 > n:
                break
            for p in range(x ** 2, n, x):
                if p in candidates:
                    candidates.remove(p)
        
        return len(candidates)
                
        