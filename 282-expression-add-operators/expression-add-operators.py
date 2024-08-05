class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        result = []

        def solve(idx: int, prev: int, curr: int, acc: int, expr: List[any]) -> None:
            if idx == N:
                if acc == target and curr == 0:
                    result.append(''.join(expr[1:]))
                return
            
            curr = curr * 10 + int(num[idx])

            if curr > 0:
                solve(idx + 1, prev, curr, acc, expr)

            str_curr = str(curr)
            
            expr.append('+')
            expr.append(str_curr)
            solve(idx + 1, curr, 0, acc + curr, expr)
            expr.pop()
            expr.pop()

            if expr:
                # -
                expr.append('-')
                expr.append(str_curr)
                solve(idx + 1, -curr, 0, acc - curr, expr)
                expr.pop()
                expr.pop()

                # *
                expr.append('*')
                expr.append(str_curr)
                solve(idx + 1, curr * prev, 0, acc - prev + (curr * prev), expr)
                expr.pop()
                expr.pop()

        solve(0, 0, 0, 0, [])
        return result