class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        lcs = [[0 for _ in range(N)] for _ in range(M)] # [text1][text2]

        for m in range(M):
            for n in range(N):
                if text1[m] == text2[n]:
                    lcs[m][n] = 1 + (lcs[m - 1][n - 1] if m > 0 and n > 0 else 0)
                else:
                    lcs[m][n] = max(lcs[m - 1][n] if m > 0 else 0, lcs[m][n - 1] if n > 0 else 0)

        return lcs[-1][-1]