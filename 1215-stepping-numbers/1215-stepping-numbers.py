class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        nums = '0123456789'
        lo_digit, hi_digit = len(str(low)), len(str(high))
        ans = []
        if low == 0:
            ans.append(0)
        
        def search(carry: str):
            if len(carry) > hi_digit:
                return
            
            num = int(carry)
            if low <= num <= high:
                ans.append(num)
            
            last_digit = int(carry[-1])
            if last_digit < 9:
                search(carry + str(last_digit + 1))
            if last_digit > 0:
                search(carry + str(last_digit - 1))
        
        for i in range(1, 10):
            search(str(i))
            
        return sorted(ans)