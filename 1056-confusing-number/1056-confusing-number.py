class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotatable = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        unrotatable = "23457"
        invalid = 'X'
        stringified = str(n)
        
        rotated = [rotatable[x] if x in rotatable else invalid for x in reversed(stringified)]
        return invalid not in rotated and ''.join(rotated) != stringified