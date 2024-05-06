class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def to_binary(x: int) -> str:
            return str(bin(x))[2:]

        def pad(x: str, y: str) -> (str, str):
            return '0' * max(0, len(y) - len(x)) + x, '0' * max(0, len(x) - len(y)) + y
        
        bab_and = to_binary(a & b)
        bab = to_binary(a | b)
        bc = to_binary(c)
        bab, bc = pad(bab, bc)
        bab_and, bc = pad(bab_and, bc)
        
        ans = 0
        for i in range(len(bab)):
            xab, xc = bab[i], bc[i]
            if xab == xc:
                continue
            if xc == 1:
                ans += 1
            else:
                if bab_and[i] == '1':
                    ans += 2
                else:
                    ans += 1

        return ans

