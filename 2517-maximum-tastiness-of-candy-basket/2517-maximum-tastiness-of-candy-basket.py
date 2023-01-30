class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        prices = sorted(price)
        N = len(prices)
        max_tastiness = 0
        
        max_achievable = prices[-1] - prices[0]
        
        lo, hi = 0, max_achievable
        
        while lo <= hi:
            x = (lo + hi) // 2
            candies = []
            for price in prices:
                if not candies or price - candies[-1] >= x:
                    candies.append(price)
            if len(candies) >= k:
                max_tastiness = max(max_tastiness, x)
                lo = x + 1
            else:
                hi = x - 1
        
        return max_tastiness
            
        
        