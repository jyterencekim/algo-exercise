class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        pt = 0
        i = 1
        while i < N:
            while nums[pt] is None:
                pt += 1
                
            if nums[pt] != nums[i]:
                nums[pt] = nums[i] = None
            i += 1
        
        for i in range(N):
            if nums[i]:
                return nums[i]