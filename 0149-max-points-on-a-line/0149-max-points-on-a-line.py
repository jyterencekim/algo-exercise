
from decimal import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def to_line(a: Tuple[int], b: Tuple[int]) -> Tuple[float]:
            # y = slope * x + y_intercept
            # returns (slope, x-intercept, y-intercept)
            x1, y1 = a
            x2, y2 = b
            if x1 == x2:
                return math.inf, None, x1
            slope = Decimal(y2 - y1) / Decimal(x2 - x1)
            y_intercept = y1 - (slope * x1)
            x_intercept = -y_intercept / slope if slope else (0 if y1 == 0 else None)
            return slope, x_intercept, y_intercept
        
        points_by_lines = defaultdict(set) # (slope, b) -> set of pts
        
        N = len(points)
        
        if N < 2:
            return 1
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                a, b = tuple(points[i]), tuple(points[j])
                line = to_line(a, b)
                points_by_lines[line].add(a)
                points_by_lines[line].add(b)
        
        return max(len(points) for points in points_by_lines.values())
            
            