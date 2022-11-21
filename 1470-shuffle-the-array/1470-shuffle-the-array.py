class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        half = len(nums) // 2
        for ptr in range(half):
            result.append(nums[ptr])
            result.append(nums[ptr + half])
        return result