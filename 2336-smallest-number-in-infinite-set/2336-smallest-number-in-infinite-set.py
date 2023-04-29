class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        # all elts <= curr
        self.added_back = []

    def popSmallest(self) -> int:
        popped = None
        if not self.added_back:
            popped = self.curr
            self.curr += 1
        else:
            popped = heapq.heappop(self.added_back)
            while self.added_back and self.added_back[0] == popped:
                heapq.heappop(self.added_back)
        return popped
        

    def addBack(self, num: int) -> None:
        if num >= self.curr:
            return
        heapq.heappush(self.added_back, num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)