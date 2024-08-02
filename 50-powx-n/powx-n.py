class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def do_pow(x: float, n: int) -> float:
            if n == 0:
                return 1
            if x == 0:
                return 0
            if n < 0:
                return 1 / do_pow(x, -n)
            if n == 1:
                return x
            if n % 2 == 0:
                return do_pow(x, n // 2) * do_pow(x, n // 2)
            return do_pow(x, n - 1) * x
        
        return do_pow(x, n)
            