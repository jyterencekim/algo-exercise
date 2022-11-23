class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        
        psum = []
        for num in nums:
            psum.append((psum[-1] if psum else 0) + num)
        
        ssums = []
        for i in range(n):
            for j in range(i, n):
                ssums.append(psum[j] - (psum[i - 1] if i > 0 else 0))
                
        ssums.sort()
        return sum(ssums[left - 1:right]) % MOD