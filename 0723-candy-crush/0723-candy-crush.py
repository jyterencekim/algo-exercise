class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        EMPTY = 0
        M, N = len(board), len(board[0])
        THRESHOLD = 3
        
        def do_crush_vertical(val: int, i: int, j: int, crushed: Set[int], count=0):
            if i >= M or board[i][j] == EMPTY or board[i][j] != val:
                if count >= THRESHOLD:
                    for v in range(count):
                        crushed.add((i - 1 - v, j))
                return count
            return do_crush_vertical(val, i + 1, j, crushed, count + 1)
        
        def do_crush_horizontal(val: int, i: int, j: int, crushed: Set[int], count=0):
            if j >= N or board[i][j] == EMPTY or board[i][j] != val:
                if count >= THRESHOLD:
                    for h in range(count):
                        crushed.add((i, j - 1 - h))
                return count
            return do_crush_horizontal(val, i, j + 1, crushed, count + 1)
        
        def make_fall(crushed: Set[int]) -> None:
            for j in range(N):
                w = M - 1
                r = M - 1
                while r >= 0:
                    while r > 0 and (r, j) in crushed:
                        r -= 1
                    board[w][j] = board[r][j] if (r, j) not in crushed else EMPTY
                    r -= 1
                    w -= 1
                while w >= 0:
                    board[w][j] = EMPTY
                    w -= 1
                    
            
        def crush() -> Set[int]:
            crushed = set()
            for i in range(M):
                for j in range(N):
                    if board[i][j] != EMPTY:
                        do_crush_vertical(board[i][j], i, j, crushed)
                        do_crush_horizontal(board[i][j], i, j, crushed)
            return crushed
        
        while True:
            crushed = crush()
            if not crushed:
                break
            make_fall(crushed)
        
        return board