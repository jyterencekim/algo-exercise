class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = list(shifts)
        N = len(s)
        for i in range(N - 2, -1, -1):
            total_shifts[i] += total_shifts[i + 1]
            
        def do_shift(x: chr, shift: int) -> chr:
            return chr(((ord(x) - ord('a') + shift) % 26) + ord('a'))
        
        result = []
        for i, x in enumerate(s):
            result.append(do_shift(x, total_shifts[i]))
            
        return ''.join(result)