class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        required = 0
        concurrent = []

        for s, e in sorted(intervals, key=lambda i:i[0]):
            while concurrent and concurrent[0][0] <= s:
                heapq.heappop(concurrent)
            heapq.heappush(concurrent, (e, s))
            required = max(required, len(concurrent))
        
        return required