class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        thirds = []
        global_max = -math.inf
        for num in nums:
            global_max = max(global_max, num)
            if num not in thirds:
                thirds = sorted(thirds + [num])[-3:]
        
        return thirds[0] if len(thirds) == 3 else thirds[-1]