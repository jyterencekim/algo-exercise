class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix_sum = [0 for _ in range(N)]
        postfix_sum = [0 for _ in range(N)]
        prefix_sum[0] = nums[0]
        postfix_sum[-1] = nums[-1]

        for i in range(1, N):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            postfix_sum[N - 1 - i] = postfix_sum[N - i] + nums[N - 1 - i]
        
        ways_unchanged = 0
        
        for pivot in range(1, N):
            left = prefix_sum[pivot - 1]
            right = postfix_sum[pivot]
            if left == right:
                ways_unchanged += 1
        
        ways_changed = 0

        """
        left - something + k == right
        or
        left == right - something + k

        We have prefix sums and postfix sums.
        We are considering the case of changing one element here ONLY.
        Does it help to keep track of frequencies (counters) of sums? Maybe.

        """
        sum_diffs = [l - r for l, r in zip(prefix_sum[:-1], postfix_sum[1:])]
        left = Counter()
        right = Counter(sum_diffs)

        for idx in range(N):
            replaced = nums[idx]
            required_diff = k - replaced
            ways = 0
            if idx > 0:
                left[sum_diffs[idx - 1]] += 1
                right[sum_diffs[idx - 1]] -= 1
            ways += left[required_diff] 
            ways += right[-required_diff]
            ways_changed = max(ways, ways_changed)
        
        return max(ways_unchanged, ways_changed)
