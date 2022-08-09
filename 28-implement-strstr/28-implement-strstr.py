class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = len(haystack), len(needle)
        lps = [0 for _ in range(N)]
        
        # Precompute the longest proper prefix/suffix length table
        longest = 0
        i = 1
        while i < N:
            if needle[i] == needle[longest]:
                longest += 1
                lps[i] = longest
                i += 1
            else:
                if longest:
                    longest = lps[longest - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        h, n = 0, 0
        while h < H and n < N:
            if haystack[h] == needle[n]:
                h += 1
                n += 1
                if n == N:
                    return h - n
            else:
                if n > 0:
                    n = lps[n - 1]
                else:
                    h += 1
            
        return -1