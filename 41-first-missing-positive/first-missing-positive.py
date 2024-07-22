class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        3, 4, -1, 1
        -> 1, ?, 3, 4
        """
        def replace(idx: int):
            start = idx
            idx = nums[start]
            tmp = nums[idx] if 0 <= idx < len(nums) else None

            while 0 <= idx < len(nums) and nums[idx] != idx:
                # swap forward
                tmp = nums[idx]
                nums[idx] = idx
                idx = tmp
                
                
        nums = [0] + nums
        for i in range(len(nums)):
            replace(i)

        for idx, val in enumerate(nums):
            if idx != val:
                return idx
        
        
        return len(nums)
