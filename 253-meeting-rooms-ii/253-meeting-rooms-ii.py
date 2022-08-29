class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        used = [] # minheap by e
        
        for s, e in intervals:
            if used and used[0] <= s:
                heapq.heappop(used)
            heapq.heappush(used, e)
            
        return len(used)
        