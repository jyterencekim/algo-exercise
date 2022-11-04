class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_efforts = [[math.inf for _ in range(COLS)] for _ in range(ROWS)]
        min_efforts[0][0] = 0
        
        def get_adjacents(r: int, c: int) -> Tuple[int]:
            if r > 0:
                yield r - 1, c
            if c > 0:
                yield r, c - 1
            if r < ROWS - 1:
                yield r + 1, c
            if c < COLS - 1:
                yield r, c + 1
        
        pq = [(0, (0, 0))]
        
        while pq:
            effort, pos = heapq.heappop(pq)
            r, c = pos
            if (r, c) == (ROWS - 1, COLS - 1):
                return effort
            for x, y in get_adjacents(r, c):
                resulting_effort = max(effort, abs(heights[x][y] - heights[r][c]))
                if resulting_effort < min_efforts[x][y]:
                    min_efforts[x][y] = resulting_effort
                    heapq.heappush(pq, (resulting_effort, (x, y)))
        
        return None