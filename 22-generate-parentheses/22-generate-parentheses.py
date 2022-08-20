class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPENING, CLOSING = '(', ')'
        ans = []
        def generate(opened: int, closed: int, stack: List[str]):
            nonlocal OPENING, CLOSING, n, ans
            can_open = n - opened
            can_close = opened - closed
            if not can_open and not can_close:
                ans.append(''.join(stack))
            if can_open:
                stack.append(OPENING)
                generate(opened + 1, closed, stack)
                stack.pop()
            if can_close:
                stack.append(CLOSING)
                generate(opened,  closed + 1, stack)
                stack.pop()
        
        generate(0, 0, [])
        return ans