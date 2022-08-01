class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        def to_map(s: str) -> dict:
            d = defaultdict(set)
            for idx, c in enumerate(s):
                d[c].add(idx)
            return d
        
        # digit -> set of pos
        secret_map, guess_map = to_map(secret), to_map(guess)
    
        
        bulls, cows = 0, 0
        for character, indices in secret_map.items():
            if character in guess_map:
                guess_indices = guess_map[character]
                matched = indices.intersection(guess_indices)
                bulls_count = len(matched)
                indices_in_secret_count = len(indices)
                lingering = guess_indices - matched
                cows_count = min(indices_in_secret_count - bulls_count, len(lingering))
                bulls += bulls_count
                cows += cows_count
                
        return f"{bulls}A{cows}B"
                