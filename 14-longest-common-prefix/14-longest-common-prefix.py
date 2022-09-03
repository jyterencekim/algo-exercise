class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        max_prefix = -1 # inclusive
        
        for idx in range(min_len):
            chars = set(s[idx] for s in strs)
            if len(chars) > 1:
                break
            max_prefix = idx
        
        return strs[0][:max_prefix + 1]