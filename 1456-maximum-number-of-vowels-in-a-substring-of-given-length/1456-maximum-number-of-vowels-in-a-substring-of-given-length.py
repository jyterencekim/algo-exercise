class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = "aeiou"
        max_vowel_count = 0
        counts = Counter()
        size = 0
        i = j = 0 # inclusive ends
        
        while j < len(s):           
            if j - i + 1 > k:
                counts[s[i]] -= 1 if s[i] in VOWELS else 0
                i += 1
            
            c = s[j]
            counts[c] += 1 if c in VOWELS else 0
            max_vowel_count = max(max_vowel_count, sum(counts.values()))
            
            if max_vowel_count == k:
                return k
            
            j += 1
        
        return max_vowel_count
            
        
        
        