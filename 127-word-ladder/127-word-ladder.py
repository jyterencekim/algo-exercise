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
        
        q_forward = deque([(beginWord, 1)])
        q_backward = deque([(endWord, 1)])
        visited_forward = { beginWord: 1 }
        visited_backward = { endWord: 1 }
        is_forward = True
        
        while q_forward and q_backward:
            if is_forward:
                q = q_forward
                visited = visited_forward
                visited_opposite = visited_backward
            else:
                q = q_backward
                visited = visited_backward
                visited_opposite = visited_forward
            is_forward = not is_forward
            
            to_consume = len(q)
            for _ in range(to_consume):
                word, dist = q.popleft()
                visited[word] = dist
            
                if word in visited_opposite:
                    return dist - 1 + visited_opposite[word]

                for adjacent in get_adjacents(word):
                    if adjacent not in visited:
                        q.append((adjacent, dist + 1))
        
        return 0