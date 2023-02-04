class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        thirds = []
        for num in nums:
            if num not in thirds:
                thirds = sorted(thirds + [num])[-3:]
        
        return thirds[0] if len(thirds) == 3 else thirds[-1]