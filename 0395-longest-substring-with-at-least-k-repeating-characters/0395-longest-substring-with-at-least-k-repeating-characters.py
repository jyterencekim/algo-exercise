class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        N = len(s)
        unique_chars = set(s)
        max_length = 0
        
        for u in range(1, len(unique_chars) + 1):
            start, end = 0, 0
            unique_carry = Counter()
            satisfied_uniques = 0
            
            while end < N:
                unique_carry[s[end]] += 1
                if unique_carry[s[end]] == k:
                    satisfied_uniques += 1
                    
                while len(unique_carry) > u:
                    if unique_carry[s[start]] == k:
                        satisfied_uniques -= 1
                    unique_carry[s[start]] -= 1
                    if unique_carry[s[start]] == 0:
                        del unique_carry[s[start]]
                    start += 1
                
                if satisfied_uniques == len(unique_carry):
                    length = end - start + 1
                    max_length = max(max_length, length)
                    
                end += 1
        
        return max_length
        
                