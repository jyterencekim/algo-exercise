class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        sum_even = []
        sum_odd = []
        
        for i, num in enumerate(nums):
            last_even = sum_even[-1] if sum_even else 0
            last_odd = sum_odd[-1] if sum_odd else 0
            if i % 2 == 0: # even
                sum_even.append(last_even + num)
                sum_odd.append(last_odd)
            else:
                sum_even.append(last_even)
                sum_odd.append(last_odd + num)
        
        ans = 0
        for i, num in enumerate(nums):
            prev_even_sum = sum_even[i - 1] if i > 0 else 0
            prev_odd_sum = sum_odd[i - 1] if i > 0 else 0
            next_even_sum = sum_even[N - 1] - sum_even[i]
            next_odd_sum = sum_odd[N - 1] - sum_odd[i]
            
            even_sum = prev_even_sum + next_odd_sum
            odd_sum = prev_odd_sum + next_even_sum
            if even_sum == odd_sum:
                ans += 1
        
        return ans
            