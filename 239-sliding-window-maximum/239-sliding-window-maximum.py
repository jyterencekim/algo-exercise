class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        
        result = []
        q = deque() # (value, index)
        
        for i, num in enumerate(nums):
            # maintenance
            while q and q[0][1] <= i - k:
                q.popleft()

            while q and q[-1][0] < num:
                q.pop()

            if not q or q[-1][0] >= num:
                q.append((num, i))
            
            if i + 1 >= k:
                result.append(q[0][0])
        
        return result
            
        