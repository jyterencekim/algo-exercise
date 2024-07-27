class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        queen - diagonal, horizontal, vertical
        n queens, n * n matrix
        - putting 1 queen determines which positions cannot be taken / to preclude
        - as we go, consider whether a given (r, c) collides with the queens already put
        - "previous" state -> queens put
        - base state -> none put

        brute force
        - n^2 Choose n
        - n^3 ?
        """
        solutions = set()

        # TODO
        def record(queens: Tuple[Tuple[int]]) -> None:
            result = []
            queens = set(queens)
            for r in range(n):
                row = []
                for c in range(n):
                    if (r, c) in queens:
                        row.append('Q')
                    else:
                        row.append('.')
                result.append(''.join(row))
            solutions.add(tuple(result))
        
        def collide(queens: Tuple[Tuple[int]], candidate: Tuple[int]) -> bool:
            r, c = candidate

            for qr, qc in queens:
                if qr == r or qc == c or abs(qr - r) == abs(qc - c):
                    return True
            
            return False

        def do_solve(queens: Tuple[Tuple[int]], r: int, c: int) -> None:
            if len(queens) == n:
                record(queens)
            if r >= n:
                return
            if c >= n:
                do_solve(queens, r + 1, 0)
                return
            # put or not put here
            if not collide(queens, (r, c)):
                do_solve(queens + ((r, c),), r, c + 1)
            do_solve(queens, r, c + 1)

        do_solve((), 0, 0)
        return solutions
