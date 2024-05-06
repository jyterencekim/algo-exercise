class MedianFinder:

    def __init__(self):
        self.left_max_heap = [] # negative
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max_heap, -num)
        heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))

        if len(self.left_max_heap) < len(self.right_min_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))
        """
        if (not self.left_max_heap and not self.right_min_heap):
            heapq.heappush(self.right_min_heap, num)
            return
        if self.right_min_heap[0] <= num:
            heapq.heappush(self.right_min_heap, num)
            if self.right_min_heap and len(self.right_min_heap) > len(self.left_max_heap) + 1:
                popped = heapq.heappop(self.right_min_heap)
                heapq.heappush(self.left_max_heap, -popped)
        else:
            heapq.heappush(self.left_max_heap, -num)
            if self.left_max_heap and len(self.left_max_heap) > len(self.right_min_heap):
                popped = heapq.heappop(self.left_max_heap)
                heapq.heappush(self.right_min_heap, -popped)
        """
        

    def findMedian(self) -> float:
        if (len(self.left_max_heap) + len(self.right_min_heap)) % 2 == 0:
            left_max = -self.left_max_heap[0] if self.left_max_heap else 0
            right_min = self.right_min_heap[0] if self.right_min_heap else 0
            
            return (float(left_max) + float(right_min)) / 2.0
        return -self.left_max_heap[0] if self.left_max_heap else None
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()