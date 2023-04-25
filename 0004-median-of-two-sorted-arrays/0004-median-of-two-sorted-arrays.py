class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1, N2 = len(nums1), len(nums2)
        N = N1 + N2
        
        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, N1
        
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = math.ceil(N / 2) - mid1
            
            l1 = nums1[mid1 - 1] if mid1 > 0 else -math.inf
            r1 = nums1[mid1] if mid1 < N1 else math.inf
            l2 = nums2[mid2 - 1] if mid2 > 0 else -math.inf
            r2 = nums2[mid2] if mid2 < N2 else math.inf
            
            if l1 > r2:
                hi = mid1 - 1
            elif l2 > r1:
                lo = mid1 + 1
            else:
                if N % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                return max(l1, l2)
            
        return None