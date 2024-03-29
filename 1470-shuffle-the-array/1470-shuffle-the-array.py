class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = len(nums) // 2
        for ptr in range(half):
            yield nums[ptr]
            yield nums[ptr + half]