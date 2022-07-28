class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(gains: List[int]) -> int:
            if not gains:
                return 0
            robbed = gains[0]
            skipped = 0
            
            for i in range(1, len(gains)):
                gain = gains[i]
                robbing = skipped + gain
                skipping = max(skipped, robbed)
                robbed, skipped = robbing, skipping
            
            return max(robbed, skipped)
        
        if len(nums) < 2:
            return max(nums)
        return max(solve(nums[1:]), solve(nums[:-1]))
                
                
            
            