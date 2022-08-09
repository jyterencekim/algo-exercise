class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H, N = len(haystack), len(needle)
        
        # longest prefix/suffix lengths for needle[0..x]
        lps = [0 for _ in range(N)]
        
        i = 1
        longest = 0
        while i < N:
            if needle[i] == needle[longest]:
                longest += 1
                lps[i] = longest
                i += 1
            else:
                if longest:
                    longest = lps[longest - 1]
                else:
                    lps[i] = longest = 0
                    i += 1
        
        
        h, n = 0, 0
        while h < H:
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
                    