class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        N = len(word)
        def get(ptr: int) -> Tuple:
            if ptr == N:
                return [[''], ['']]
            
            kept = set()
            abbreviated = set()
            
            for i in range(ptr, N):
                original_prefix = word[ptr:i + 1]
                abbreviated_prefix = str(i - ptr + 1)
                
                postfixes = get(i + 1)
                nons, abbrs = postfixes
                    
                for non in nons:
                    kept.add(original_prefix + non)
                    abbreviated.add(abbreviated_prefix + non)
                for abbr in abbrs:
                    kept.add(original_prefix + abbr)
                
            return kept, abbreviated
        
        results = get(0)
        return results[0].union(results[1])
            
            