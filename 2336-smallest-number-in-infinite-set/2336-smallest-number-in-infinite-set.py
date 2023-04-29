class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        # all elts <= curr
        self.added_back = set()
        self.added_back_heap = []

    def popSmallest(self) -> int:
        popped = None
        if not self.added_back:
            popped = self.curr
            self.curr += 1
        else:
            popped = heapq.heappop(self.added_back_heap)
            self.added_back.remove(popped)
        return popped
        

    def addBack(self, num: int) -> None:
        if num >= self.curr:
            return
        if num not in self.added_back:
            self.added_back.add(num)
            heapq.heappush(self.added_back_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)