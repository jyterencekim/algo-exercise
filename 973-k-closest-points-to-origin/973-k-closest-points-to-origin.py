class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]) -> float:
            x, y = point
            return math.sqrt(x ** 2 + y ** 2)
        distances_and_points = [(distance(point), point) for point in points]
        
        def partition(lo: int, hi: int) -> int:
            """
            returns the pivot's resulting index
            """
            nonlocal distances_and_points
            l = distances_and_points
            
            random_index = random.randint(lo, hi)
            pivot = l[random_index]
            l[hi], l[random_index] = l[random_index], l[hi]
            frontier = lo
            # pivot is now at l[hi]
            for i in range(lo, hi):
                if l[i][0] <= pivot[0]:
                    l[frontier], l[i] = l[i], l[frontier]
                    frontier += 1
            # [lte] - frontier - [gt]
            l[frontier], l[hi] = l[hi], l[frontier]
            
            return frontier
        
        N = len(points)
        lo, hi = 0, N - 1
        
        while lo <= hi:
            pivot_index = partition(lo, hi)
            order = pivot_index + 1
            if order == k:
                return [distance_and_point[1] for distance_and_point in distances_and_points[:k]]
            elif order < k:
                lo = pivot_index + 1
            else:
                hi = pivot_index - 1
        