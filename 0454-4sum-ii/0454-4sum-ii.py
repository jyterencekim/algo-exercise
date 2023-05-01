class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        a = Counter()
        b = Counter()
        
        for x in nums1:
            for y in nums2:
                a[x + y] += 1
        
        for x in nums3:
            for y in nums4:
                b[x + y] += 1
        
        counts = 0
        
        for x, xs in a.items():
            if -x in b:
                counts += (xs * b[-x])
        
        return counts