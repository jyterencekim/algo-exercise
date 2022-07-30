class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs/bfs and increment the count upon a newly discovered (unvisited) cell
        ROWS, COLS = len(grid), len(grid[0])
        LAND, WATER = "1", "0"
        
        island_count = 0
        visited = set()
        
        def get_adjacents(row: int, col: int) -> Tuple[int]:
            if row > 0:
                yield (row - 1, col)
            if col > 0:
                yield (row, col - 1)
            if row < ROWS - 1:
                yield (row + 1, col)
            if col < COLS - 1:
                yield (row, col + 1)
                
        def explore(row: int, col: int):
            nonlocal visited
            to_visit = [(row, col)]
            
            while to_visit:
                r, c = to_visit.pop()
                visited.add((r, c))
                
                for new_r, new_c in get_adjacents(r, c):
                    if (new_r, new_c) not in visited and grid[new_r][new_c] == LAND:
                        to_visit.append((new_r, new_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r, c) not in visited:
                    island_count += 1
                    explore(r, c)
        
        return island_count
                    