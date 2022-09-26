class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x: Tuple[int], y: Tuple[int]) -> int:
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        # Kruskal
        roots = dict()
        for x, y in points:
            roots[(x, y)] = (x, y)
            
        def find_root(p: Tuple[int]) -> Tuple[int]:
            if roots[p] != p:
                roots[p] = find_root(roots[p])
            return roots[p]
        
        def connect(p1: Tuple[int], p2: Tuple[int]) -> Tuple[int]:
            roots[find_root(p1)] = find_root(p2)
            return find_root(p1)
            
        def are_connected(p1, p2) -> bool:
            return find_root(p1) == find_root(p2)
        
        edges = [] # heap
        for i, p1 in enumerate(points):
            for j in range(i + 1, len(points)):
                p2 = points[j]
                heapq.heappush(edges, (distance(p1, p2), tuple(p1), tuple(p2)))
        
        to_connect = len(points)
        cost_acc = 0
        
        while to_connect > 1:
            d, p1, p2 = heapq.heappop(edges)
            if not are_connected(p1, p2):
                connect(p1, p2)
                cost_acc += d
                to_connect -= 1
        
        return cost_acc
            