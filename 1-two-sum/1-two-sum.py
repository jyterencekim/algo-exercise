class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = { num: i for i, num in enumerate(nums) }
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_indices and nums_indices[complement] != i:
                return [i, nums_indices[complement]]
        return []
            
        