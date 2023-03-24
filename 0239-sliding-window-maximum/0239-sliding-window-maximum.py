class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window = deque()
        result = []
        
        for i, num in enumerate(nums):
            while window and window[-1][1] < num:
                window.pop()
            window.append((i, num))
            if window and window[0][0] <= i - k:
                window.popleft()
            result.append(window[0][1])
            
        return result[k - 1:]
            
        