class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        START, FOOD, FREE, OBSTACLE = '*', '#', 'O', 'X'
        
        start = None
        
        ROWS, COLS = len(grid), len(grid[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == START:
                    start = (row, col)
                    break        
        
        q = deque([(start, 0)]) # (row, col), dist
        visited = set()
        
        def get_adjacents(pos: Tuple[int]) -> Tuple[int]:
            r, c = pos
            if r + 1 < ROWS:
                yield r + 1, c
            if c + 1 < COLS:
                yield r, c + 1
            if r > 0:
                yield r - 1, c
            if c > 0:
                yield r, c - 1
        
        visited.add(start)
        while q:
            pos, d = q.popleft()
            r, c = pos
            if grid[r][c] == FOOD:
                return d
            
            for next_pos in get_adjacents(pos):
                x, y = next_pos
                if next_pos not in visited and grid[x][y] != OBSTACLE:
                    visited.add(next_pos)
                    q.append((next_pos, d + 1))
        
        return -1