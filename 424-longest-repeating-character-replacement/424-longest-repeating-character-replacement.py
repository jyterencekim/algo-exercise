class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = Counter()
        most_freq = 0
        start = 0
        
        for end, c in enumerate(s):
            freq[c] += 1
            most_freq = max(most_freq, freq[c])
            
            while (end - start + 1) - most_freq > k:
                freq[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, (end - start + 1))
        
        return max_len
                
                                
                    