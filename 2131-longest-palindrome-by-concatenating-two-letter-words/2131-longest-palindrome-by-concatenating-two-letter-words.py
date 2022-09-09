class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        left = Counter(words)
        specials = { word for word in words if word[0] == word[1] }
        longest = 0
        words_set = set(words)
        
        for word in words_set:
            rev = word[::-1]
            if word in specials:
                if left[word] >= 2:
                    pairable = left[word] // 2
                    longest += pairable * 4 
                    left[word] -= pairable * 2
            elif left[word] and left[rev]:
                usable = min(left[word], left[rev])
                longest += usable * 4
                left[word] -= usable
                left[rev] -= usable
        
        for word in specials:
            if left[word]:
                longest += 2
                break
                
        return longest