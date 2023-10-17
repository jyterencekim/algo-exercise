class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subarray_sum = 0
        max_avg = -math.inf
        
        for i, num in enumerate(nums):
            subarray_sum += num
            if i >= k:
                subarray_sum -= nums[i - k]
            if i >= k - 1:
                max_avg = max(max_avg, subarray_sum / k)
        
        return max_avg
        
        
        