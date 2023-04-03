
from decimal import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # lines can be defined by their x,y-intercepts and their slope
        def get_y_intercept(point: Tuple[int], slope: float) -> float:
            x, y = point
            
            if slope == math.inf:
                if x == 0:
                    return 0
                return None
            
            return y - (slope * x)
        
        def get_x_intercept(point: Tuple[int], slope: float, y_intercept: float) -> float:
            x, _ = point
            if not slope or slope == math.inf or not y_intercept:
                return x
                
            return -y_intercept / slope
        
        def get_slope(a: Tuple[int], b: Tuple[int]) -> float:
            ax, ay = a
            bx, by = b
            diff_x = bx - ax
            diff_y = by - ay
            
            if diff_x == 0:
                return math.inf
            
            return Decimal(diff_y) / Decimal(diff_x)
        
        points_by_lines = defaultdict(set) # (slope, b) -> set of pts
        
        N = len(points)
        
        if N < 2:
            return 1
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                a, b = tuple(points[i]), tuple(points[j])
                slope = get_slope(a, b)
                y_intercept = get_y_intercept(a, slope)
                x_intercept = get_x_intercept(a, slope, y_intercept)
                points_by_lines[(slope, x_intercept, y_intercept)].add(a)
                points_by_lines[(slope, x_intercept, y_intercept)].add(b)
        
        print(points_by_lines)
        
        return max(len(points) for points in points_by_lines.values())
            
            