class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x:x[0])
        booked = Counter()
        h = [(0, r) for r in range(n)] # (available_at, room_number)
        heapq.heapify(h)
        
        for s, e in meetings:
            next_h = []
            candidates = []
            selected = None
            
            while h:
                available_at, room = heapq.heappop(h)
                if available_at <= s:
                    heapq.heappush(candidates, (room, available_at))
                else: 
                    heapq.heappush(next_h, (available_at, room))
            
            if not candidates:
                available_at, room = heapq.heappop(next_h)
                selected = (available_at + (e - s), room)
                booked[room] += 1
            else:
                room, available_at = heapq.heappop(candidates)
                selected = (e, room)
                booked[room] += 1

            while candidates:
                room, available_at = heapq.heappop(candidates)
                heapq.heappush(next_h, (available_at, room))

            heapq.heappush(next_h, selected)
            h = next_h
        
        return max(booked.keys(), key=lambda k:(booked[k], -k))

