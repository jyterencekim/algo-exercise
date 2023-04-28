class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l, h = math.ceil(low / 2), math.ceil(high / 2)
        # 3 -> 1,3; 7 -> 1,3,5,7
        
        if low % 2 == 1:
            return h - l + 1
        return h - l