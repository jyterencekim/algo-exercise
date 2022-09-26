class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        min_dist = [math.inf for _ in range(N)]
        
        # starting point
        mst = { tuple(points[0]) }
        min_dist[0] = 0
        
        def get_distance(a, b) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        frontier = tuple(points[0])
        while len(mst) < N:
            optimal_dist, closest = math.inf, None
            for j, y in enumerate(points):
                if tuple(y) not in mst:
                    min_dist[j] = min(min_dist[j], get_distance(frontier, y))
                    if min_dist[j] < optimal_dist:
                        optimal_dist, closest = min_dist[j], y
                
            mst.add(tuple(closest))
            frontier = tuple(closest)
        
        return sum(min_dist)