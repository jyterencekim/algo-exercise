class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr = 0 # exclusive prefix end
        
        if not strs:
            return ""
        
        can_proceed = True
        while can_proceed:
            x = None
            for s in strs:
                if ptr >= len(s):
                    can_proceed = False
                    break
                y = s[ptr]
                if not x:
                    x = y
                elif x != y:
                    can_proceed = False
                    break
            ptr += can_proceed
        
        return strs[0][:ptr]