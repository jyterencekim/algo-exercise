class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        N = len(nums)
        
        candidate = None
        
        for i in range(N - 2):
            x = nums[i]
            j = i + 1
            k = N - 1
            
            while j < k:
                y, z = nums[j], nums[k]
                choice = x + y + z
                if choice == target:
                    return target
                if choice < target:
                    j += 1
                else:
                    k -= 1
                
                if candidate is None or abs(target - candidate) > abs(target - choice):
                    candidate = choice
                
        
        return candidate
    
                