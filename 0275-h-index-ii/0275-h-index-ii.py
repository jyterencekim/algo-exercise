class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        lo, hi = 0, N - 1
        candidate = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            count_gte = N - mid

            if citations[mid] == count_gte:
                return count_gte
            elif citations[mid] < count_gte:
                lo = mid + 1
            else:
                hi = mid - 1
            
        return N - lo
        