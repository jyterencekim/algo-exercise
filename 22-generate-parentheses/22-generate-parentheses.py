class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPENING, CLOSING = '(', ')'
        def generate(opened: int, closed: int) -> str:
            nonlocal OPENING, CLOSING, n
            can_open = n - opened
            can_close = opened - closed
            if not can_open and not can_close:
                yield ''
            if can_open:
                for sub in generate(opened + 1, closed):
                    yield OPENING + sub
            if can_close:
                for sub in generate(opened,  closed + 1):
                    yield CLOSING + sub
        
        yield from generate(0, 0)