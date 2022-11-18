class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = Counter(s)
        
        result = []
        for k, f in freqs.most_common():
            result.append(k * f)
        
        return ''.join(result)