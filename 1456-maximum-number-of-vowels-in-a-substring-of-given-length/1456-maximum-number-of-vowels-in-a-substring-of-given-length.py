class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = set("aeiou")
        max_vowel_count = 0
        count = 0
        
        for right in range(len(s)):
            left = right - k + 1
            if left > 0:
                count -= 1 if s[left - 1] in VOWELS else 0
            count += 1 if s[right] in VOWELS else 0
            max_vowel_count = max(max_vowel_count, count)
            
            if max_vowel_count == k:
                return k
            
        
        return max_vowel_count
            
        
        
        