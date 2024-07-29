class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @cache
        def check(p1: int, p2: int, p3: int) -> bool:
            if p1 == len(s1) and p2 == len(s2):
                return p3 == len(s3)
            if p3 == len(s3):
                return p1 == len(s1) and p2 == len(s2)
            
            c1 = s1[p1] if p1 < len(s1) else None
            c2 = s2[p2] if p2 < len(s2) else None
            c3 = s3[p3]
            if c1 == c2 == c3:
                return check(p1 + 1, p2, p3 + 1) or check(p1, p2 + 1, p3 + 1)
            if c1 == c3:
                return check(p1 + 1, p2, p3 + 1)
            if c2 == c3:
                return check(p1, p2 + 1, p3 + 1)
            return False
        
        return check(0, 0, 0)

        
            
        
