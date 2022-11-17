class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        def get_distance(x: chr, y: chr) -> Tuple:
            a, b = ord(x) - ord('a'), ord(y) - ord('a')
            diff = b - a
            if diff < 0:
                return 26 + diff
            return diff
            
        moves = Counter()
        
        for i in range(1, 26):
            moves[i] = k // 26
        for i in range(1, k % 26 + 1):
            moves[i] += 1
            
        diffs = [get_distance(s[i], t[i]) for i in range(len(s))]
        
        for d in diffs:
            if d == 0:
                continue
            if moves[d] <= 0:
                return False
            moves[d] -= 1

        
        return True