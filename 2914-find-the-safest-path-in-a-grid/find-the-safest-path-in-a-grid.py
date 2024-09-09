class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        calculate the safeness factor for each cell
        and then perform dijkstra from (0, 0) to (n - 1, n - 1)
        """
        safeness = dict()
        N = len(grid)

        def get_manhattan_distance(src: Tuple[int], dst: Tuple[int]) -> int:
            a, b = src
            x, y = dst
            return abs(a - x) + abs(b - y)
        
        def get_adjacents(pos: Tuple[int]) -> Generator[Tuple[int], None, None]:
            x, y = pos
            if x > 0:
                yield x - 1, y
            if y > 0:
                yield x, y - 1
            if x + 1 < N:
                yield x + 1, y
            if y + 1 < N:
                yield x, y + 1

        def propagate(thief_positions: List[Tuple[int]]):
            queue = deque(thief_positions)
            visited = set()

            while queue:
                pos, dist = queue.popleft()
                visited.add(pos)
                if pos not in safeness or safeness[pos] > dist:
                    safeness[pos] = dist
                    for adj in get_adjacents(pos):
                        if adj not in visited:
                            queue.append((adj, dist + 1))
                            visited.add(adj)

        thieves = []        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    thieves.append(((r, c), 0))
        propagate(thieves)
        
        def can_satisfy(desired: int) -> bool:
            q = deque([(0, 0)])
            visited = set()

            while q:
                pos = q.popleft()
                visited.add(pos)
                if safeness[pos] < desired:
                    continue
                if pos == (N - 1, N - 1):
                    return True
                for adj in get_adjacents(pos):
                    if adj not in visited:
                        q.append(adj)
                        visited.add(adj)
            
            return False
        
        lo, hi = min(safeness.values()), max(safeness.values())

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_satisfy(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo - 1
                