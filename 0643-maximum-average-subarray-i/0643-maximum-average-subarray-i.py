class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subarray_sum = sum(nums[:k])
        max_avg = subarray_sum / k
        
        for i in range(k, len(nums)):
            subarray_sum -= nums[i - k]
            subarray_sum += nums[i]
            max_avg = max(max_avg, subarray_sum / k)
        
        return max_avg
        
        
        