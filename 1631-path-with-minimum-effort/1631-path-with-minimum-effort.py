class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # does it help to be greedy? may not be so at the end.
        # let's just consider some paths ... let's say we have two paths, of effort E1 and effort E2.
        # if those paths can be connected, then the combined path's effort will be max(E1, E2) 
        ROWS, COLS = len(heights), len(heights[0])
        
        # generator
        def get_adjacents(r: int, c: int) -> Tuple[int]:
            if r > 0:
                yield (r - 1, c)
            if c > 0:
                yield (r, c - 1)
            if r < ROWS - 1:
                yield (r + 1, c)
            if c < COLS - 1:
                yield (r, c + 1)
        
        # priority queue of (effort, r, c)
        q_by_effort = [(0, 0, 0)] 
        min_efforts = defaultdict(lambda: math.inf)
        
        while q_by_effort:
            effort_so_far, r, c = heapq.heappop(q_by_effort)
            
            if (r, c) == (ROWS - 1, COLS - 1):
                return effort_so_far
            
            for ar, ac in get_adjacents(r, c):
                effort_to_adjacent = max(abs(heights[r][c] - heights[ar][ac]), effort_so_far)
                if effort_to_adjacent < min_efforts[(ar, ac)]:
                    min_efforts[(ar, ac)] = effort_to_adjacent
                    heapq.heappush(q_by_effort, (effort_to_adjacent, ar, ac))
        
                    
        
        