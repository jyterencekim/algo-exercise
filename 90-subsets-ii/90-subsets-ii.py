class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        def subset(ptr: int, carry: Tuple[int]) -> None:
            if ptr >= len(nums):
                nonlocal answer
                answer.add(carry)
                return
            subset(ptr + 1, carry)
            subset(ptr + 1, carry + (nums[ptr],))
        
        subset(0, tuple())
        return answer
            