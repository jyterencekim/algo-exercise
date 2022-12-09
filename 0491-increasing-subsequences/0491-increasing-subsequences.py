class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ss = set()
        
        for num in nums:
            next_ss = set(ss)
            next_ss.add((num,))
            for s in ss:
                if s[-1] <= num:
                    next_ss.add(s + (num,))
            ss = next_ss
        
        return { s for s in ss if len(s) >= 2 }
        