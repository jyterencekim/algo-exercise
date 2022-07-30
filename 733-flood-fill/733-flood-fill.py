class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def get_adjacents(r: int, c: int):
            for dr, dc in DIRECTIONS:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS:
                    yield (r + dr, c + dc)
        
        # dfs/bfs
        # start searching from [sr, sc] fill in `new_color` in every reachable cells from there
        # take care of already visited cells
        
        visited = set()
        stack = [(sr, sc)]
        target_color = image[sr][sc]
        
        while stack:
            r, c = stack.pop()
            visited.add((r, c))
            image[r][c] = new_color
            for nr, nc in get_adjacents(r, c):
                if (nr, nc) not in visited and image[nr][nc] == target_color:
                    stack.append((nr, nc))
        
        return image
        