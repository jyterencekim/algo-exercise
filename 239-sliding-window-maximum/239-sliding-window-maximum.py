class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        class MaxWindowStream:
          def __init__(self, window_size=3):
            self.window_size = window_size
            self.window_heap = [(float('inf'), 0)] 
            self.current_index = 0


          def input(self, value):
            # Determine the inclusive lower bound for the valid index
            # in order to delete old data from the heap 
            valid_index_lower_bound = self.current_index - self.window_size + 1

            # Keep popping until we find the max with a valid index
            while self.window_heap and self.window_heap[0][1] < valid_index_lower_bound:
              heapq.heappop(self.window_heap)

            new_node = (-value, self.current_index)
            self.current_index += 1
            heapq.heappush(self.window_heap, new_node)

            max_within_window = -self.window_heap[0][0]
            return max_within_window
        
        result = list()
        stream = MaxWindowStream(k)
        for i in range(k - 1):
            stream.input(nums[i])
        
        for num in nums[k - 1:]:
            result.append(stream.input(num))
            
        return result