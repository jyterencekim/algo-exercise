class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs_and_indices = deque([cost, i] for i, cost in enumerate(costs))
        total_cost = 0
        heap = [] # minheap
        LEFT, RIGHT = 0, 1

        i = 0
        while costs_and_indices and i < candidates:
            heapq.heappush(heap, (costs_and_indices.popleft(), LEFT))
            i += 1
        i = 0
        while costs_and_indices and i < candidates:
            heapq.heappush(heap, (costs_and_indices.pop(), RIGHT))
            i += 1

        for round in range(k):
            (min_cost, _), direction = heapq.heappop(heap)
            total_cost += min_cost

            if costs_and_indices:
                if direction == LEFT:
                    heapq.heappush(heap, (costs_and_indices.popleft(), LEFT))
                else:
                    heapq.heappush(heap, (costs_and_indices.pop(), RIGHT))
            

        return total_cost            
