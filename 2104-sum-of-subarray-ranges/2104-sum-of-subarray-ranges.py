class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        range_sum = 0
        N = len(nums)
        for i in range(N):
            smallest = largest = nums[i]
            for j in range(i + 1, N):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                range_sum += (largest - smallest)
        
        return range_sum