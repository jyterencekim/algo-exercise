class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        freq = Counter([c.lower() for c in licensePlate if c.isalpha()])
        
        def completes(x: str) -> bool:
            return not +(freq - Counter(x))
        
        result = None
        
        for word in words:
            if completes(word):
                if not result or len(result) > len(word):
                    result = word
                
        return result
            