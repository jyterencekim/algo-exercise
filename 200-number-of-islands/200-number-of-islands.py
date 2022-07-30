class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs/bfs and increment the count upon a newly discovered (unvisited) cell
        ROWS, COLS = len(grid), len(grid[0])
        LAND, WATER = "1", "0"
        
        island_count = 0
        visited = set()
        
        def explore(row: int, col: int):
            nonlocal visited
            to_visit = [(row, col)]
            
            while to_visit:
                r, c = to_visit.pop()
                visited.add((r, c))
                
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited and grid[new_r][new_c] == LAND:
                        to_visit.append((new_r, new_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r, c) not in visited:
                    island_count += 1
                    explore(r, c)
        
        return island_count
                    