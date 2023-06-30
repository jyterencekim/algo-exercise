class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        N = len(s)
        words = []
        
        for i in range(N - 1, -1, -1):
            c = s[i]
            if c == ' ':
                if stack:
                    words.append(''.join(reversed(stack)))
                    stack = []
            else:
                stack.append(c)
        
        if stack:
            words.append(''.join(reversed(stack)))
        return ' '.join(words)
                    