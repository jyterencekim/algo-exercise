class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        W1 = len(word1)
        W2 = len(word2)
        dp = [[0 for _ in range(W2 + 1)] for _ in range(W1 + 1)]
        
        for i in range(W1 + 1):
            dp[i][0] = i
        
        for j in range(W2 + 1):
            dp[0][j] = j
            
        for i in range(1, W1 + 1):
            for j in range(1, W2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                
        return dp[-1][-1]