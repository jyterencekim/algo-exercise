class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        def hides(p1, p2) -> bool:
            # true iff. p1 hides p2
            ax, ay = p1
            bx, by = p2
            
            if ax == bx:
                return ay >= by
            
            slope = (by - ay) / (bx - ax)
            if ax < bx:
                return slope <= -1
            return slope >= 1
        
        visibles = []
        peaks = sorted(peaks, key=lambda p: p[0])
        c = Counter([tuple(p) for p in peaks])
        
        for p in peaks:
            while visibles and hides(p, visibles[-1]):
                visibles.pop()
            if not visibles or not hides(visibles[-1], p):
                visibles.append(p)
            
        
        return len([v for v in visibles if c[tuple(v)] == 1])
                    