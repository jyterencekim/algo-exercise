class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = {()}
        
        for num in nums:
            generated = set(subsets)
            for s in subsets:
                generated.add(s + (num,))
            subsets = generated
            
        return subsets
            