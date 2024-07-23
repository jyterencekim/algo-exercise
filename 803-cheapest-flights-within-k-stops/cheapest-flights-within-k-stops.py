class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        - based on the flights, construct a directed graph # s -> set(d)
        - maintain a heap where each entity = (total price, current city)
        - while min-heap in relation to the total price, pop from the heap 
          - reached dst? return the total price
          - otherwise, for each adjacent city of the city, if not visited
            - push to the heap (total price + price[curr, adj], adj)
            - visited.add(adj)
        - return -1
        """
        connections = defaultdict(set)
        for x, y, p in flights:
            connections[x].add((y, p))
        mh = [(0, 0, src)] # price, stop
        visited = {src}
        min_steps = dict()
        optimal = math.inf
        while mh:
            total, step, curr = heapq.heappop(mh)
            if curr == dst:
                return total
            if step > min_steps.get(curr, math.inf) or step > k:
                continue
            min_steps[curr] = step
            for connection, price in connections[curr]:
                if connection not in visited:
                    heapq.heappush(mh, (total + price, step + 1, connection))

        return -1
