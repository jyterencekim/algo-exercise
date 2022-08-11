class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        if N > M:
            return ""
        
        remaining = Counter(t)
        remaining_chars = len(remaining.keys())
        original = Counter(t)
        
        # inclusive range
        lo = hi = 0
        min_length = math.inf
        ans = (-1, -1)
        
        while lo < M and hi < M:
            # expand as much as possible until we get all the necessary chars
            while remaining_chars and hi < M:
                char = s[hi]
                if original[char]:
                    remaining[char] -= 1
                    if not remaining[char]:
                        remaining_chars -= 1
                hi += 1
            
                        
            while not remaining_chars and lo < hi:
                removed = s[lo]
                # update the length
                length = hi - lo
                if length < min_length:
                    ans = (lo, hi)
                    min_length = length
                lo += 1
                remaining[removed] += 1 if removed in original else 0
                remaining_chars += 1 if remaining[removed] == 1 else 0
                while lo < hi and not original[s[lo]]:
                    lo += 1
            
        return s[ans[0]:ans[1]]
                    
                
            