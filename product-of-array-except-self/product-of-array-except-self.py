class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products_from_left = [1 for _ in range(N)]
        products_from_right = [1 for _ in range(N)]
        result = [1 for _ in range(N)]
        for left in range(N):
            right = N - 1 - left
            lefts = (products_from_left[left - 1] if left > 0 else 1)
            products_from_left[left] = nums[left] * lefts
            rights = (products_from_right[right + 1] if right < N - 1 else 1)
            products_from_right[right] = nums[right] * rights
            result[left] *= lefts
            result[right] *= rights

        return result