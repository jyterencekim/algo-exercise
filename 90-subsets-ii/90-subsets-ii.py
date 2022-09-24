class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        subsets = {()}
        
        for num, count in counts.items():
            generated = set(subsets)
            for c in range(1, count + 1):
                for s in subsets:
                    generated.add(s + (num,) * c)
            subsets = generated
            
        return subsets
            