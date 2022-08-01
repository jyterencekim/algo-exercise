class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_indices:
                if nums_indices[complement] != i:
                    return [i, nums_indices[complement]]
            else:
                nums_indices[num] = i
        return []
            
        