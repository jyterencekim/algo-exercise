class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or len(needle) > len(haystack):
            return -1
        
        reader, comparer = 0, 0
        
        while reader < len(haystack):
            if haystack[reader] == needle[comparer]:
                comparer += 1
            else:
                reader -= comparer
                comparer = 0
            
            if comparer == len(needle):
                return reader - comparer + 1
            
            reader += 1
        
        return -1