class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        global_min = 0
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS, COLS = len(grid), len(grid[0])
        
        rottens = deque([]) # (pos, elapsed)
        freshes = set()
        seen = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    rottens.append((r, c, 0))
                elif grid[r][c] == FRESH:
                    freshes.add((r, c))
                    
        while rottens:
            r, c, t = rottens.popleft()
            global_min = max(global_min, t)
            
            for rd, cd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + rd, c + cd
                if (nr, nc) in freshes and 0 <= nr < ROWS and 0 <= nc < COLS:
                    freshes.remove((nr, nc))
                    rottens.append((nr, nc, t + 1))
        
        return global_min if not freshes else -1