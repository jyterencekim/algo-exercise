class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ROOM = 4
        customers = deque(customers)
        
        waiting = 0
        rotations = 0
        idx = 0
        profit_acc = 0
        max_profit = 0
        max_profit_at = -1
        
        while customers or waiting:
            rotations += 1
            customer = customers.popleft() if customers else 0
            waiting += customer
            
            boardable = min(ROOM, waiting)
            waiting -= boardable
            
            profit_acc += ((boardingCost * boardable) - runningCost)
            if profit_acc > 0 and max_profit < profit_acc:
                max_profit = profit_acc
                max_profit_at = rotations
        
        return max_profit_at