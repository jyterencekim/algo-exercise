class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        to_insert = newInterval
        result = []
        
        def overlap(x, y) -> bool:
            xs, xe = x
            ys, ye = y
            return xs <= ys <= xe or ys <= xs <= ye
        
        def merge(x, y):
            xs, xe = x
            ys, ye = y
            return min(xs, ys), max(xe, ye)
        
        tail = 0
        for i, x in enumerate(intervals):
            if not overlap(x, to_insert):
                if to_insert[1] < x[0]:
                    tail = i
                    break
                result.append(x)
                tail = i + 1
            else:
                to_insert = merge(x, to_insert)
                tail = i + 1
        
        result.append(to_insert)
        result.extend(intervals[tail:])
        return result
                