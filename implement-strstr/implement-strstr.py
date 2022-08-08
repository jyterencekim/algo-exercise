class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        
        ptr_h = ptr_n = 0
        
        while ptr_h < len(haystack) and ptr_n < len(needle):
            if haystack[ptr_h] == needle[ptr_n]:
                ptr_h += 1
                ptr_n += 1
            else:
                ptr_h += -ptr_n + 1
                ptr_n = 0
            if ptr_n == len(needle):
                return ptr_h - ptr_n
        
        return -1
                