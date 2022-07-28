class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(gains: List[int]) -> int:
            if not gains:
                return 0
            robbed = [gains[0]]
            skipped = [0]
            
            for i in range(1, len(gains)):
                gain = gains[i]
                rob = skipped[-1] + gain
                skip = max(skipped[-1], robbed[-1])
                robbed.append(rob)
                skipped.append(skip)
            
            return max(robbed[-1], skipped[-1])
        
        if len(nums) < 2:
            return max(nums)
        return max(solve(nums[1:]), solve(nums[:-1]))
                
                
            
            