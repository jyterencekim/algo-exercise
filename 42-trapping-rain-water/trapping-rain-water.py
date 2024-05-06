class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        ans = 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] <= h:
                top = stack.pop()
                if not stack:
                    break
                width = i - stack[-1][0] - 1
                height = min(h, stack[-1][1]) - top[1]
                ans += width * height
            stack.append((i, h))
        
        return ans