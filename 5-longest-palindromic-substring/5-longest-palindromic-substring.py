class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        S = len(s)
        
        def expand(l: int, r: int) -> str:
            while 0 <= l and r < S and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        for center in range(S):
            s1 = expand(center, center)
            s2 = expand(center, center + 1)
            longest = max(longest, s1, s2, key=len)
            
                    
        return longest
                
            