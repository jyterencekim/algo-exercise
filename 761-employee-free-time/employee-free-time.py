"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for s in schedule:
            for interval in s:
                intervals.append(interval)
        intervals.sort(key=lambda x:x.start)
        free_times = []

        running = None
        for interval in intervals:
            if not running:
                running = interval
                continue
            if running.end < interval.start: 
                # disparate
                free_times.append(Interval(running.end, interval.start))
                running.start = interval.start
                running.end = interval.end
            else:
                running.end = max(running.end, interval.end)
        
        return free_times