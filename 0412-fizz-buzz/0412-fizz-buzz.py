class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def convert(x: int) -> str:
            if x % 3 == 0 and x % 5 == 0:
                return "FizzBuzz"
            if x % 3 == 0:
                return "Fizz"
            if x % 5 == 0:
                return "Buzz"
            return str(x)
        return [convert(x) for x in range(1, n + 1)]