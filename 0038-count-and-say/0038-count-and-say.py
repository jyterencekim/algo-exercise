class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def say(x: str) -> str:
            if not x:
                return ""
            
            said = []
            ptr = 0
            pivot = 0
            count = 0
            while ptr < len(x):
                if x[ptr] != x[pivot]:
                    said.append(f"{count}{x[pivot]}")
                    pivot = ptr
                    count = 0
                ptr += 1
                count += 1
            if count:
                said.append(f"{count}{x[pivot]}")
            return ''.join(said)
        
        return say(self.countAndSay(n - 1))
    