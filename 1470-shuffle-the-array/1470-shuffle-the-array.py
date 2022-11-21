class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        l, r = 0, len(nums) // 2
        while r < len(nums):
            result.append(nums[l])
            result.append(nums[r])
            l += 1
            r += 1
        return result