class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        bat, tab, cat -> tabbat, battab
        bat, ab -> batab
        """
        dictionary = {word: idx for idx, word in enumerate(words)}

        def get_valid_prefixes(word: str) -> Generator[str, None, None]:
            for i in range(len(word)):
                suffix = word[i:]
                if suffix == suffix[::-1]:
                    yield word[:i]
        
        def get_valid_suffixes(word: str) -> Generator[str, None, None]:
            for i in range(len(word)):
                prefix = word[:i+1]
                if prefix == prefix[::-1]:
                    yield word[i+1:]

        result = []
        for idx, word in enumerate(words):
            rev = word[::-1]
            if rev in dictionary and dictionary[rev] != idx:
                result.append((idx, dictionary[rev]))
            for prefix in get_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in dictionary:
                    result.append((idx, dictionary[reversed_prefix]))
            for suffix in get_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in dictionary:
                    result.append((dictionary[reversed_suffix], idx))
        
        return result
