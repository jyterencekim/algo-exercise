class Solution:
    def beautySum(self, s: str) -> int:
        def calculate_beauty(counts: dict) -> int:
            min_c, max_c = None, None
            min_freq, max_freq = math.inf, -math.inf
            
            for c, freq in counts.items():
                if freq == 0:
                    continue
                if freq > max_freq:
                    max_c, max_freq = c, freq
                if freq < min_freq:
                    min_c, min_freq = c, freq
            
            if min_c != max_c:
                return max_freq - min_freq
            return 0
            return max(counts.values()) - min(counts.values())
        
        beauty_sum = 0
        
        for offset in range(1, len(s)):
            counts = Counter(s[:offset+1])
            beauty_sum += calculate_beauty(counts)
            
            for left in range(1, len(s) - offset):
                right = left + offset
                counts[s[left - 1]] -= 1
                counts[s[right]] += 1
                beauty_sum += calculate_beauty(counts)
        
        return beauty_sum
                