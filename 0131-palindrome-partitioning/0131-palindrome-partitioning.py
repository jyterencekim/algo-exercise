class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        results = []
        def backtrack(start: int, carry: List[str]):
            if start >= len(s):
                results.append(list(carry))
            for end in range(start, len(s)):
                portion = s[start:end + 1]
                if portion == portion[::-1]:
                    carry.append(s[start:end + 1])
                    backtrack(end + 1, carry)
                    carry.pop()
        
        backtrack(0, [])
        return results
        