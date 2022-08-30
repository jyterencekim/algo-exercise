class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        word_lengths = sorted(list(len(word) for word in words))
        L = len(s)
        breakable = [False for _ in range(L)] + [True]
        
        for index in range(L, -1, -1):
            # true iff. there is a word + the tail is breakable
            for length in word_lengths:
                tail_index = index + length
                if tail_index > L:
                    break
                head = s[index:index + length]
                if head in words and breakable[tail_index]:
                    breakable[index] = True
                    break
        
        return breakable[0]
                