# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def is_previous_good(idx: int) -> bool:
            return not isBadVersion(idx - 1) if idx > 0 else True
        def is_bad(idx: int) -> bool:
            return isBadVersion(idx)
        
        lo, hi = 1, n
        
        while lo <= hi:
            mid = (lo + hi) // 2    
            prev_good = is_previous_good(mid)
            now_bad = is_bad(mid)
            
            if prev_good and is_bad(mid):
                return mid
            if prev_good:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return 1
            