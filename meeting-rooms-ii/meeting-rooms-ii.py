class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        opened = [] # minheap by e
        max_concurrent = 0
        
        for s, e in intervals:
            while opened and opened[0] <= s:
                heapq.heappop(opened)
            heapq.heappush(opened, e)
            max_concurrent = max(max_concurrent, len(opened))
            
        return max_concurrent
        