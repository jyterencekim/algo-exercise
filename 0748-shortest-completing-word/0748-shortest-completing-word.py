class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required_freq = Counter([c.lower() for c in licensePlate if c.isalpha()])
        
        def completes(x: str) -> bool:
            freq = Counter(x)
            for c, f in required_freq.items():
                if freq[c] < f:
                    return False
            return True
        
        result = None
        
        for word in words:
            if completes(word) and (not result or len(result) > len(word)):
                result = word
                
        return result
            