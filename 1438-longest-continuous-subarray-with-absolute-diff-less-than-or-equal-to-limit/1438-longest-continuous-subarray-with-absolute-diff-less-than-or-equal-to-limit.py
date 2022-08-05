class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        def solve(nums: List[int], limit: int) -> int:
            """
            Approach 2.
            you can keep expanding a window as long as the new item does not affect the max-min diff.
            slide the window if the current max-min diff > limit.
            slide => left++. if left > right, right++
            keep track of the longest window
            """
            L = len(nums)
            if L < 2:
                return L
            
            left, right = 0, -1
            max_length = 1
            
            window_maxs = []
            window_mins = []
                           
            while left < L:
                if left > right:
                    right = left
                    window_maxs = [(-nums[left], left)]
                    window_mins = [(nums[left], left)]
                    
                window_max, max_at = window_maxs[0]
                window_min, min_at = window_mins[0]
                window_max = -window_max
                diff = window_max - window_min
                
                if diff <= limit:
                    max_length = max(max_length, right - left + 1)
                    if right + 1 == L:
                        break
                    right += 1
                    pushed = nums[right]
                    heapq.heappush(window_maxs, (-pushed, right))
                    heapq.heappush(window_mins, (pushed, right))
                else:
                    popped = nums[left]
                    left += 1
                    while window_maxs[0][1] < left:
                        heapq.heappop(window_maxs)
                    while window_mins[0][1] < left:
                        heapq.heappop(window_mins)
                
            return max_length
        
        return solve(nums, limit)