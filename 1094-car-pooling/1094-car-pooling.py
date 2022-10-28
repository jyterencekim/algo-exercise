class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = defaultdict(int)

        for np, s, e in trips:
            changes[s] += np
            changes[e] -= np
        
        carry = 0
        for pt in sorted(changes.keys()):
            carry += changes[pt]
            if carry > capacity:
                return False
        
        return True
