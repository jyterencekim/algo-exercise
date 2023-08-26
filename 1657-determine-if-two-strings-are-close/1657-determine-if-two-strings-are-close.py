class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)

        freqs_a = Counter(vs for k, vs in a.items())
        freqs_b = Counter(vs for k, vs in b.items())

        return a.keys() == b.keys() and freqs_a == freqs_b