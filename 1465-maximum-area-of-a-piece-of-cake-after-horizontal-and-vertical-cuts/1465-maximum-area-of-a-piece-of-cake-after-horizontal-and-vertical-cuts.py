class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        widths = []
        heights = []
        
        prev = 0
        for cut in sorted(verticalCuts):
            width = cut - prev
            prev = cut
            widths.append(width)
        widths.append(w - prev)
        
        prev = 0
        for cut in sorted(horizontalCuts):
            height = cut - prev
            prev = cut
            heights.append(height)
        heights.append(h - prev)
        
        widths.sort(reverse=True)
        heights.sort(reverse=True)
        
        print(heights, widths)
        
        return (widths[0] * heights[0]) % MOD
        
        
        