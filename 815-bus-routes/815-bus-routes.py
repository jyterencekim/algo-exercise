class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        buses_for_stop = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                buses_for_stop[stop].add(bus)
        
        if not buses_for_stop[target]:
            return -1
        
        to_take = deque([(bus, 1) for bus in buses_for_stop[source]])
        taken = set()
        
        while to_take:
            bus, transfer_count = to_take.popleft()
            if bus in buses_for_stop[target]:
                # guaranteed to be the minimum transfer count
                return transfer_count
            
            stops = routes[bus]
            available_buses = { b for stop in stops for b in buses_for_stop[stop] }
            
            for connecting_bus in available_buses:
                if connecting_bus not in taken:
                    to_take.append((connecting_bus, transfer_count + 1))
                    taken.add(connecting_bus)
        
        return -1
            