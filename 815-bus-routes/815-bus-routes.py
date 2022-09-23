class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # no need for route sequences
        for i, route in enumerate(routes):
            routes[i] = set(route)
        
        # bus -> bus
        connections = defaultdict(set)
        
        BUSES = len(routes)
        for bus_a in range(BUSES - 1):
            # base
            connections[bus_a].add(bus_a)
            for bus_b in range(bus_a + 1, BUSES):
                for stop in routes[bus_a]:
                    if stop in routes[bus_b]:
                        connections[bus_a].add(bus_b)
                        connections[bus_b].add(bus_a)
                        break
        
        answer = math.inf
        to_take = deque([(bus, 1) for bus in range(BUSES) if source in routes[bus]])
        taken = set()
        
        while to_take:
            bus, transfer_count = to_take.popleft()
            if target in routes[bus]:
                # guaranteed to be the minimum transfer count
                return transfer_count
            
            for connecting_bus in connections[bus]:
                if connecting_bus not in taken:
                    to_take.append((connecting_bus, transfer_count + 1))
                    taken.add(connecting_bus)
        
        return -1
            