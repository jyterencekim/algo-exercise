class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs_and_indices = deque((cost, i) for i, cost in enumerate(costs))
        total_cost = 0
        left, right = [], []

        while costs_and_indices and len(left) < candidates:
            heapq.heappush(left, costs_and_indices.popleft())
        while costs_and_indices and len(right) < candidates:
            heapq.heappush(right, costs_and_indices.pop())

        for round in range(k):
            left_min, left_idx = heapq.heappop(left) if left else (math.inf, -1)
            right_min, right_idx = heapq.heappop(right) if right else (math.inf, -1)
            
            print(left_min, left_idx, right_min, right_idx)
            if left_min <= right_min:
                total_cost += left_min
                heapq.heappush(right, (right_min, right_idx))
                if costs_and_indices:
                    heapq.heappush(left, costs_and_indices.popleft())
            else:
                total_cost += right_min
                heapq.heappush(left, (left_min, left_idx))
                if costs_and_indices:
                    heapq.heappush(right, costs_and_indices.pop())
                

        return total_cost            
