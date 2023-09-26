class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        S = len(word1)
        T = len(word2)
        
        if S == 0 or T == 0:
            return max(S, T)
        
        dists = [[math.inf for _ in range(S + 1)] for _ in range(T + 1)]
        
        for s in range(S):
            dists[0][s] = s
        for t in range(T):
            dists[t][0] = t
        
        for t in range(1, T + 1):
            for s in range(1, S + 1):
                replaced = dists[t - 1][s - 1]
                deleted = dists[t][s - 1]
                added = dists[t - 1][s]
                
                if word1[s - 1] == word2[t - 1]:
                    dists[t][s] = replaced
                else:
                    dists[t][s] = min(deleted, added, replaced) + 1
        
        return dists[-1][-1]