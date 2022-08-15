from itertools import chain

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        relatives = defaultdict(set)
        ANY = '*'
        
        def to_relatives(x: str):
            for i in range(len(x)):
                yield x[:i] + ANY + x[i + 1:]
        
        def get_adjacents(x: str):
            nonlocal relatives
            result = []
            for relative in to_relatives(x):
                yield from relatives[relative]
            
        
        words = set(wordList)
        words.add(beginWord)
        
        if endWord not in words:
            return 0
        
        for a in words:
            for rel in to_relatives(a):
                relatives[rel].add(a)
        
        q = deque([(endWord, 1)])
        visited = set()
        
        while q:
            word, dist = q.popleft()
            visited.add(word)
            
            if word == beginWord:
                return dist
            
            for adjacent in get_adjacents(word):
                if adjacent not in visited:
                    q.append((adjacent, dist + 1))
        
        return 0