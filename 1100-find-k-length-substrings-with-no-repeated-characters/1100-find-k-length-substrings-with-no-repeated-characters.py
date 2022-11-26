class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        N = len(s)
        if k > N:
            return 0
        repeated = set()
        nonrepeated = 0
        counter = Counter(s[:k])
        
        for c, count in counter.items():
            if count > 1:
                repeated.add(c)
        
        if not repeated:
            nonrepeated += 1
        
        for head in range(1, N - k + 1):
            tail = head + k - 1
            
            new_char = s[tail]
            removed_char = s[head - 1]
            counter[removed_char] -= 1
            counter[new_char] += 1
            
            if removed_char in repeated and counter[removed_char] <= 1:
                repeated.remove(removed_char)
            if counter[new_char] > 1:
                repeated.add(new_char)
            
            if not repeated:
                nonrepeated += 1
                
        return nonrepeated