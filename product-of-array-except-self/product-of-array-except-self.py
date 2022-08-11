class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products_from_left = [1 for _ in range(N)]
        products_from_right = [1 for _ in range(N)]
        result = [None for _ in range(N)]
        for left in range(N):
            right = N - 1 - left
            products_from_left[left] = nums[left] * (products_from_left[left - 1] if left > 0 else 1)
            products_from_right[right] = nums[right] * (products_from_right[right + 1] if right < N - 1 else 1)
        
        for i in range(N):
            left = products_from_left[i - 1] if i > 0 else 1
            right = products_from_right[i + 1] if i < N - 1 else 1
            result[i] = left * right

        return result