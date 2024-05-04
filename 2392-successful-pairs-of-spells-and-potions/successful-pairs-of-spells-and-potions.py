class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def search(gte: int, lo: int, hi: int) -> int:
            # bisect by lte, returned index = # of failing pairs
            return bisect.bisect_left(potions, gte)
        
        result = []
        P = len(potions)
        potions.sort()

        for spell in spells:
            needed = math.ceil(success / spell)
            r = P - search(needed, 0, P)
            result.append(r)
            
        return result

