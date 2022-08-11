class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secrets = Counter(secret)
        
        bulls = cows = 0
        for idx, char in enumerate(guess):
            if char in secrets:
                if char == secret[idx]:
                    bulls += 1
                    if secrets[char] <= 0:
                        cows -= 1
                elif secrets[char] > 0:
                    cows += 1
                secrets[char] -= 1
                
                
        return f"{bulls}A{cows}B"
                
                