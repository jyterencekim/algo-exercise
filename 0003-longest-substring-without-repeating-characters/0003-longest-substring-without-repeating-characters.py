class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        lo, hi = 0, 0
        longest = 0
        
        for hi in range(len(s)):
            if s[hi] in seen:
                lo = max(lo, seen[s[hi]] + 1)
            seen[s[hi]] = hi
            longest = max(longest, hi - lo + 1)
        
        return longest
        
        