class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        [9, 2, 2, / 15, 11, 15, 27] k = 4
        for a given index, keep track of the max sum
        dp[i] = dp[i - j] + max(arr[j + 1 ... i]) * j for j in [1..k]
        """
        N = len(arr)
        dp = [0 for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(1, k + 1):
                if i - j < 0:
                    break
                dp[i] = max(dp[i], dp[i - j] + max(arr[i-j:i]) * j)

        return dp[-1]