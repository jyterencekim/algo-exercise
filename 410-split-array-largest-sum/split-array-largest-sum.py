class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        for num in nums:
            if not prefix_sum:
                prefix_sum.append(num)
                continue
            prefix_sum.append(prefix_sum[-1] + num)
        
        @cache
        def solve(remaining_k: int, upper_bound: int) -> int:
            # upper_bound is inclusive
            if remaining_k == 1:
                return prefix_sum[upper_bound]
            
            if remaining_k - 2 >= upper_bound:
                return math.inf

            return min(max(solve(remaining_k - 1, i - 1), prefix_sum[upper_bound] - prefix_sum[i - 1]) for i in range(upper_bound + 1))
        
        return solve(k, len(nums) - 1)