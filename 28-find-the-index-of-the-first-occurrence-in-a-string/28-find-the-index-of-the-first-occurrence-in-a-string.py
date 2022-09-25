class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or len(needle) > len(haystack):
            return -1
        
        H, N = len(haystack), len(needle)
        lps = [0 for _ in range(N)]
        
        # precompute lps
        max_len = 0        
        for i in range(1, N):
            while max_len and needle[max_len] != needle[i]:
                max_len = lps[max_len - 1]
            if needle[max_len] == needle[i]:
                max_len += 1
                lps[i] = max_len        
        
        reader, comparer = 0, 0
        while reader < H and comparer < N:
            if haystack[reader] == needle[comparer]:
                comparer += 1
                reader += 1
            elif comparer:
                comparer = lps[comparer - 1]
            else:
                reader += 1
            
        return reader - comparer if comparer == N else -1