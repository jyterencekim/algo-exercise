class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        O, X = 'O', 'X'
        def get_adjacents(r: int, c: int):
            return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
        
        def is_outside(r: int, c: int) -> bool:
            return r < 0 or c < 0 or r >= ROWS or c >= COLS
        
        def fill(r: int, c: int, visited: Set[Tuple]) -> bool:
            if (r, c) in visited:
                return True
            
            visited.add((r, c))
        
            is_valid = True
            for x, y in get_adjacents(r, c):
                if is_outside(x, y):
                    return False
                if board[x][y] == O and (x, y) not in visited:
                    is_valid = is_valid and fill(x, y, visited)
            
            return is_valid
                
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == O:
                    visited = set()
                    is_valid = fill(r, c, visited)
                    
                    if is_valid:
                        for x, y in visited:
                            board[x][y] = X
