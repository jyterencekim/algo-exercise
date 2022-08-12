class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        max_from_left = max_from_right = [None for _ in range(N)]
        left_max = right_max = -math.inf
        left_max_at = right_max_at = None
        
        left, right = 0, N - 1
        max_volume = 0
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            max_volume = max(max_volume, volume)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
            
        return max_volume
            