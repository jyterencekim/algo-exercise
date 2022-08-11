class Solution:
    def isValid(self, s: str) -> bool:
        OPENINGS = "({["
        CLOSINGS = ")}]"
        BRACKETS = set(OPENINGS + CLOSINGS)
        matches = { closer: OPENINGS[i] for i, closer in enumerate(CLOSINGS) }
        
        stack = []
        for c in s:
            if c not in BRACKETS:
                continue
            if c in CLOSINGS:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != matches[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack