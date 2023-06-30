class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        cits = sorted(citations, reverse=True)
        N = len(cits)
        i = 0
        while i < N and cits[i] >= i + 1:
            i += 1
        
        return i