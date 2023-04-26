class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [tuple(x) for x in points]
        
        @cache
        def get_distance(point: Tuple[int]) -> int:
            x, y = point
            return math.sqrt(x ** 2 + y ** 2)
        
        def get_kth(lo: int, hi: int, relative_k_zero: int) -> Tuple[int]:
            while lo <= hi:
                # inclusive lo, hi
                random_index = random.randint(lo, hi)
                pivot = points[random_index]
                points[hi], points[random_index] = points[random_index], points[hi]
                # pivot at hi
                frontier = lo
                for pt in range(lo, hi):
                    if get_distance(points[pt]) <= get_distance(pivot):
                        points[pt], points[frontier] = points[frontier], points[pt]
                        frontier += 1

                points[frontier], points[hi] = points[hi], points[frontier]
                relative_pos = frontier - lo
                if relative_pos == relative_k_zero:
                    return points[:frontier + 1]
                elif relative_pos < relative_k_zero:
                    lo = frontier + 1
                    relative_k_zero -= (relative_pos + 1)
                else:
                    hi = frontier - 1
                
        
        return get_kth(0, len(points) - 1, k - 1)
                