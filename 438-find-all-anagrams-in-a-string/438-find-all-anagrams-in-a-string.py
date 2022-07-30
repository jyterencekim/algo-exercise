class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S, P = len(s), len(p)
        
        if P > S:
            return []
        
        window = Counter(s[:P])
        target_counter = Counter(p)
        answer = []
        
        for starting_point in range(S - P + 1):
            if starting_point > 0:
                window[s[starting_point - 1]] -= 1
                window[s[starting_point + P - 1]] += 1
            if window == target_counter:
                answer.append(starting_point)
                
        return answer
                
        