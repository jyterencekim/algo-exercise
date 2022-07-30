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

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND and (r, c) not in visited:
                    island_count += 1
                    to_visit = [(r, c)]
            
                    while to_visit:
                        x, y = to_visit.pop()
                        visited.add((x, y))
                        for new_r, new_c in get_adjacents(x, y):
                            if (new_r, new_c) not in visited and grid[new_r][new_c] == LAND:
                                to_visit.append((new_r, new_c))
        
        return island_count
                    