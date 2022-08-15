from itertools import chain

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        relatives = defaultdict(set)
        ANY = '*'
        
        def to_relatives(x: str) -> List[str]:
            return [x[:i] + ANY + x[i + 1:] for i in range(len(x))]
        
        def are_adjacents(a: str, b: str) -> bool:
            return len([c for i, c in enumerate(a) if c != b[i]]) == 1
        
        def get_adjacents(x: str) -> List[str]:
            nonlocal relatives
            result = []
            for relative in to_relatives(x):
                result += relatives[relative]
            return result
            
        
        words = set(wordList)
        words.add(beginWord)
        
        if endWord not in words:
            return 0
        
        for a in words:
            for rel in to_relatives(a):
                relatives[rel].add(a)
        
        q = deque([(beginWord, 1)])
        visited = set()
        
        while q:
            word, dist = q.popleft()
            visited.add(word)
            
            if word == endWord:
                return dist
            
            for adjacent in get_adjacents(word):
                if adjacent not in visited:
                    q.append((adjacent, dist + 1))
        
        return 0