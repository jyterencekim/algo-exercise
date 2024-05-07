class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        last_valid = None

        intervals = sorted(intervals, key=lambda interval:interval[1])

        for idx, interval in enumerate(intervals):
            if not last_valid or last_valid[1] <= interval[0]:
                last_valid = interval
            else:
                removed += 1
        
        return removed
            