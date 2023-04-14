class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        lo, hi = 1, x
        
        while lo <= hi:
            mid = (lo + hi) // 2
            power = mid ** 2
            
            if power == x:
                return mid
            elif power < x:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi
        