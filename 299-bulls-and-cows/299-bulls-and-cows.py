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
        for character, secret_indices in secret_map.items():
            secrets_count = len(secret_indices)
            if character in guess_map:
                guess_indices = guess_map[character]
                matched = secret_indices.intersection(guess_indices)
                bulls_count = len(matched)
                remaining = guess_indices - matched
                cows_count = min(secrets_count - bulls_count, len(remaining))
                bulls += bulls_count
                cows += cows_count
                
        return f"{bulls}A{cows}B"
                