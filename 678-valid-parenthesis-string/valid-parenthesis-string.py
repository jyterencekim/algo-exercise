class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = [] # idx, c
        wildcards = [] # idx

        # * can be interpreted differently later?

        for idx, c in enumerate(s):
            if c == '*':
                wildcards.append(idx)
            if c == ')':
                if not stack or stack[-1][1] != '(':
                    if wildcards:
                        wildcards.pop()
                        continue
                    return False
                stack.pop()
            if c == '(':
                stack.append((idx, c))

        if not stack:
            return True
        
        """
        permissible
        (((***
        ***)))
        """
        while wildcards and stack:
            wildcard_idx = wildcards.pop()
            idx, c = stack.pop()
            if c == '(' and wildcard_idx < idx:
                return False
            if c == ')' and wildcard_idx > idx:
                return False
        
        return not stack
        