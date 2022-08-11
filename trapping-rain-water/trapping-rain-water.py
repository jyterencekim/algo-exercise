class Solution:
    def trap(self, height: List[int]) -> int:
        H = len(height)
        max_at = max((i for i in range(H)), key=lambda idx: height[idx])
        
        def accumulate(heights: List[int]) -> int:
            acc = 0
            max_height = -math.inf
            for h in heights:
                if max_height < h:
                    max_height = h
                else:
                    acc += max_height - h
            return acc
        
        return accumulate(height[:max_at]) + accumulate(reversed(height[max_at + 1:]))
                