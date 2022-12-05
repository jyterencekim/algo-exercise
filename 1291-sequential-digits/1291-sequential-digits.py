class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        SEQ = '123456789'
        lo_d = int(math.log(low, 10))
        hi_d = int(math.log(high, 10))
        
        # tenth
        for d in range(lo_d, hi_d + 1):
            for head in range(len(SEQ) - d):
                seq = int(SEQ[head:head+d+1])
                if low <= seq <= high:
                    yield seq
                    