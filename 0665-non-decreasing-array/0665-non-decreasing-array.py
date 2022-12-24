class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        tolerated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]: # problematic
                if tolerated:
                    return False
                if i == len(nums) - 1 or nums[i - 1] <= nums[i + 1]:
                    tolerated = True
                    nums[i] = nums[i - 1] # FIXME: side-effect
                elif i - 1 == 0 or nums[i - 2] <= nums[i]:
                    tolerated = True
                else:
                    return False
        
        return True