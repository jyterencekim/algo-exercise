class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        L = len(word)
        chars = set(word)
        chars_at = defaultdict(set)
        
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                if char in chars:
                    chars_at[char].add((r, c))
        
        def get_adjacents(r, c):
            if r > 0:
                yield (r - 1, c)
            if c > 0:
                yield (r, c - 1)
            if r < ROWS - 1:
                yield (r + 1, c)
            if c < COLS - 1:
                yield (r, c + 1)
        
        
        def explore(r: int, c: int, pt: int, visited: set):
            if board[r][c] != word[pt]:
                return False
            if pt == L - 1:
                return True
            
            chars_left = L - 1 - pt
            is_within_reach = True
            for char in set(word[pt + 1:]):
                is_within_reach = is_within_reach and any(abs(x - r) + abs(y - c) <= chars_left for (x, y) in chars_at[char]) 
            
            if not is_within_reach:
                return False
            
            visited.add((r, c))
            result = any(explore(x, y, pt + 1, visited) for x, y in get_adjacents(r, c) if (x, y) not in visited)
            visited.remove((r, c))
            return result
        
        for r in range(ROWS):
            for c in range(COLS):
                result = explore(r, c, 0, set())
                if result:
                    return True
        
        return False
            