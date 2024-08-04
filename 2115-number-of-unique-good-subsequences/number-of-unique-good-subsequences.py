class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        0
        not empty, no leading zeroes
        all good subsequences' counts

        zero -> special case
        for each idx, constructible[idx] = sigma i = [0 .. idx - 1] for constructible[i]

        ends by 1? ends by 0?
        e.g. 

        dp[i][0][0] = dp[i][0][1] = 0

        if binary[idx] = 1
            for l in range(1, idx + 1):
                dp[idx][l][1] = dp[idx - 1][l - 1][1] + dp[idx - 1][l - 1][0]
                dp[idx][l][0] = dp[idx - 1][l][0]
        else
            for l in range(1, idx + 1):
                dp[idx][l][0] = (dp[idx - 1][l - 1][0] if l - 1 > 1 else 0) + dp[idx - 1][l - 1][1]
                dp[idx][l][1] = dp[idx - 1][l][1]

        return sum(dp[-1][l][0] + dp[-1][l][0] for l in range(len(binary)))

        """

        MOD = 10**9 + 7
        @cache
        def solve(idx: int) -> Tuple[int]: 
            # ends with zero, ends with one, leading zero
            if idx == 0:
                if binary[idx] == '0':
                    return 0, 0, 1
                return 0, 1, 0
            
            ends_with_zero, ends_with_one, leading_zero = solve(idx - 1)
            if binary[idx] == '1':
                return ends_with_zero, (ends_with_zero + ends_with_one + 1) % MOD, leading_zero
            return (ends_with_zero + ends_with_one) % MOD, ends_with_one, leading_zero
        
        ans = solve(len(binary) - 1)
 
        return (ans[0] + ans[1] + min(1, ans[0] + ans[2])) % MOD