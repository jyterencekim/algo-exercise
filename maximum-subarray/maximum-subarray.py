class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = accumulated = renewed = nums[0]
        
        for num in nums[1:]:
            accumulated = max(accumulated, renewed) + num
            renewed = num
            largest_sum = max(largest_sum, accumulated, renewed)
        
        return largest_sum
            