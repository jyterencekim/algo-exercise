import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if (r, c) == (0, 0):
                    ways[r][c] = 1
                    continue
                ways_from_up = ways[r - 1][c] if r > 0 else 0
                ways_from_left = ways[r][c - 1] if c > 0 else 0
                ways[r][c] = ways_from_up + ways_from_left
        
        return ways[-1][-1]