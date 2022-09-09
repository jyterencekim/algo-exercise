class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        left = Counter(words)
        specials = { word for word in words if word[0] == word[1] }
        longest = 0
        
        for word in words:
            rev = word[::-1]
            if word in specials:
                if left[word] >= 2:
                    longest += 4
                    left[word] -= 2
            elif left[word] and left[rev]:
                longest += 4
                left[word] -= 1
                left[rev] -= 1
        
        for word in specials:
            if left[word]:
                longest += 2
                break
                
        return longest