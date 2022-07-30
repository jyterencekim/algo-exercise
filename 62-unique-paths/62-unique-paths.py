import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ways of choosing m's and n's within (m - 1) and (n - 1)
        all_combinations = math.perm(m + n - 2)
        interchangeable_m = math.perm(m - 1)
        interchangeable_n = math.perm(n - 1)
        
        return all_combinations // interchangeable_m // interchangeable_n