class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or len(needle) > len(haystack):
            return -1
        
        H, N = len(haystack), len(needle)
        lps = [0 for _ in range(N)]
        
        # precompute lps
        max_len = 0
        i = 1
        
        while i < N:
            if needle[max_len] == needle[i]:
                max_len += 1
                lps[i] = max_len
                i += 1
            else:
                if max_len:
                    max_len = lps[max_len - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        
        reader, comparer = 0, 0
        
        while reader < H:
            if haystack[reader] == needle[comparer]:
                comparer += 1
                reader += 1
            else:
                if comparer:
                    comparer = lps[comparer - 1]
                else:
                    reader += 1
                
            if comparer == len(needle):
                return reader - comparer
            
        
        return -1