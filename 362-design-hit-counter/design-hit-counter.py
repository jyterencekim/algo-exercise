WINDOW_SECONDS = 300

class HitCounter:

    def __init__(self):
        self.hits = deque() # ts
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] + WINDOW_SECONDS <= timestamp:
            self.hits.popleft()
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)