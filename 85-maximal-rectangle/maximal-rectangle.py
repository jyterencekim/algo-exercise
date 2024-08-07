class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        lens = [[0 for _ in range(C)] for _ in range(R + 1)]

        for r in range(R):
            for c in range(C - 1, -1, -1):
                if matrix[r][c] == '1':
                    prev = lens[r][c + 1] if c < C - 1 else 0
                    lens[r][c] = 1 + prev

        max_area = 0

        for c in range(C):
            stack = []
            for r in range(R + 1):
                top = r
                while stack and stack[-1][0] > lens[r][c]:
                    prev_w, top = stack.pop()
                    area = prev_w * (r - top)
                    max_area = max(max_area, area)
                stack.append((lens[r][c], top))
        
        return max_area
