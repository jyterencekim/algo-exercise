class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        lens = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C - 1, -1, -1):
                if matrix[r][c] == '1':
                    prev = lens[r][c + 1] if c < C - 1 else 0
                    lens[r][c] = 1 + prev

        max_area = 0

        for r in range(R):
            for c in range(C):
                if lens[r][c]:
                    running_width = lens[r][c]
                    max_area = max(max_area, running_width)            
                    for nr in range(r + 1, R):
                        running_width = min(running_width, lens[nr][c])
                        if not running_width:
                            break
                        height = nr - r + 1
                        running_area = height * running_width
                        max_area = max(max_area, running_area)
        
        return max_area
