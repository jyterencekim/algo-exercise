class Solution:
    def trap(self, height: List[int]) -> int:
        def accumulate(hs: List[int]) -> int:
            highest = 0
            acc = 0
            for h in hs:
                highest = max(highest, h)
                gain = highest - h
                acc += gain
            return acc
        max_at = height.index(max(height))
        return accumulate(height[:max_at]) + accumulate(reversed(height[max_at:]))
                