class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        N = len(word)
        result = []
        def backtrack(ptr: int, abbr: int, carry: List[chr]) -> Tuple:
            if ptr == N:
                result.append(''.join(carry) + (str(abbr) if abbr else ''))
                return
            
            carry_len = len(carry)
            
            # kept
            if abbr:
                carry.append(str(abbr))
            carry.append(word[ptr])
            backtrack(ptr + 1, 0, carry)
            
            while len(carry) > carry_len:
                carry.pop()
            
            # abbreviated
            backtrack(ptr + 1, abbr + 1, carry)
            
            while len(carry) > carry_len:
                carry.pop()
        
        backtrack(0, 0, [])
        return result
            
            