class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        THRESHOLD = 2
        def is_compatible(x: str, y: str) -> bool:
            # assuming equal lengths
            dist = 0
            for idx, c in enumerate(x):
                dist += (c != y[idx])
                if dist > THRESHOLD:
                    return False
            return True
        
        for query in queries:
            for d in dictionary:
                if is_compatible(query, d):
                    yield query
                    break
                    