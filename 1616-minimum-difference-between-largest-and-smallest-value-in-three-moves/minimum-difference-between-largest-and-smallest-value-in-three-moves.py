class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def determine(lo: int, hi: int, remaining_moves: int) -> int:
            if lo == hi:
                return 0
            if remaining_moves == 0:
                return nums[hi] - nums[lo]
            return min(determine(lo + 1, hi, remaining_moves - 1), determine(lo, hi - 1, remaining_moves - 1))

        nums.sort()
        return determine(0, len(nums) - 1, 3)