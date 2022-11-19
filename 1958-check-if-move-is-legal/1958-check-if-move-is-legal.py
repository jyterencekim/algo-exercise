class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        EMPTY = '.'
        board[rMove][cMove] = '!'
        
        # for b in board:
        #     print(b)
        
        def is_empty(r, c) -> bool:
            return not (0 <= r < ROWS) or not (0 <= c < COLS) or board[r][c] == EMPTY
        
        def is_good(r: int, c: int, rd: int, cd: int, end_color: str, length: int):
            if is_empty(r, c):
                return False
            if board[r][c] == end_color:
                return length >= 3 # and is_empty(r + rd, c + cd)
            return is_good(r + rd, c + cd, rd, cd, end_color, length + 1)
        
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        return any(is_good(rMove + rd, cMove + cd, rd, cd, color, 2) for rd, cd in DIRECTIONS)
            