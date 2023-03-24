class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        COLORS = [0, 1]
        frontier = 0
        
        if not nums:
            return
        
        for c in COLORS:
            pt = frontier
            for pt in range(len(nums)):
                if nums[pt] == c:
                    nums[frontier], nums[pt] = nums[pt], nums[frontier]
                    frontier += 1
        