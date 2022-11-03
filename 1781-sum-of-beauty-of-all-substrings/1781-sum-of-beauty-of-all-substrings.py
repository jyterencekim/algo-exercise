class Solution:
    def beautySum(self, s: str) -> int:
        def beautify(freqs: List[int]) -> int:
            return max(freqs) - min(f for f in freqs if f)
        def to_ord(c: chr) -> int:
            return ord(c) - ord('a')
        
        beauty_sum = 0
        S = len(s)
        for left in range(S - 1):
            freqs = [0] * 26
            for right in range(left, S):
                freqs[to_ord(s[right])] += 1
                beauty_sum += beautify(freqs)
                
        
        return beauty_sum
                