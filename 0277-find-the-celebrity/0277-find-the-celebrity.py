# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            is_celebrity = True
            for j in range(n):
                if i == j:
                    continue
                if not knows(j, i) or knows(i, j):
                    is_celebrity = False
                    break
            if is_celebrity:
                return i
        
        return -1