class Solution:
    def numTilings(self, n: int) -> int:
        whole = [0, 1, 2]
        upper = [0, 0, 1]
        lower = [0, 0, 1]
        
        if n < 3:
            return n
        
        MOD = 10**9 + 7
        
        for i in range(3, n + 1):
            new_whole = whole[-2] + whole[-1] + lower[-1] + upper[-1]
            new_upper = whole[-2] + lower[-1]
            new_lower = whole[-2] + upper[-1]
            whole.append(new_whole % MOD)
            upper.append(new_upper % MOD)
            lower.append(new_lower % MOD)

        return whole[-1]
            