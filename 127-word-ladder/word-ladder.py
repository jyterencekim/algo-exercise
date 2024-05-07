class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0
        
        WILDCARD = '*'
        wildcarded = defaultdict(set) # wildcarded key -> key's adjacents

        def wildcardify(word: str) -> str:
            for i, c in enumerate(word):
                yield word[:i] + WILDCARD + word[i+1:]

        for word in words:
            for wildcardified in wildcardify(word):
                wildcarded[wildcardified].add(word)

        # bfs
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for wildcardified in wildcardify(word):
                for adj in wildcarded[wildcardified]:
                    if word == adj:
                        continue
                    if adj not in seen:
                        q.append((adj, dist + 1))
                        seen.add(word)
        
        return 0
