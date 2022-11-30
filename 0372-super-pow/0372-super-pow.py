class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        D = 1337
        patterns = []
        
        for x in range(1, 10 ** len(b)):
            pattern = (a ** x) % D
            if pattern in patterns:
                break
            patterns.append(pattern)
        
        freq = len(patterns)
        pt = -1
        
        for digit, bi in enumerate(reversed(b)):
            progress = bi * (10 ** digit)
            pt = (pt + progress) % freq
        
        if pt == -1:
            return 1
        
        return patterns[pt]