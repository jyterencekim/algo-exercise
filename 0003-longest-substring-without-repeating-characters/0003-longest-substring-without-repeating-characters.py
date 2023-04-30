class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lo, hi = 0, 0
        longest = 0
        
        while hi < len(s):
            while s[hi] in seen:
                seen.remove(s[lo])
                lo += 1
            seen.add(s[hi])
            length = hi - lo + 1
            longest = max(longest, length)
            hi += 1
        
        return longest
        
        