class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        detonated_by = defaultdict(set)

        def detonates(a: List[int], b: List[int]) -> bool:
            ax, ay, ar = a
            bx, by, _ = b
            return abs(ax - bx)**2 + abs(ay - by)**2 <= ar**2

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                a, b = bombs[i], bombs[j]
                if detonates(a, b):
                    detonated_by[i].add(j)
        
        max_explosions = 0
        
        def bfs(i: int) -> int:
            q = deque([i])
            visited = {i}
            while q:
                curr = q.popleft()
                for detonated in detonated_by[curr]:
                    if detonated not in visited:
                        q.append(detonated)
                        visited.add(detonated)
            
            return len(visited)

        for i in range(N):
            max_explosions = max(max_explosions, bfs(i))

        return max_explosions