class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        class TrieNode:
            def __init__(self, char=None):
                self.char = char
                self.word = None
                self.parent = None
                self.nexts = dict()
            def prune(self):
                node = self
                node.word = None
                parent = node.parent
                while parent and len(node.nexts) == 0:
                    del parent.nexts[node.char]
                    node = parent
                    parent = parent.parent
        
        def insert(root: TrieNode, word: str):
            for c in word:
                if c not in root.nexts:
                    root.nexts[c] = TrieNode()
                child = root.nexts[c]
                child.char = c
                child.parent = root
                root = child
            root.word = word
            
        trie_root = TrieNode()
        for word in words:
            insert(trie_root, word)
        
        max_len = max(len(word) for word in words)
        ROWS, COLS = len(board), len(board[0])
        found = set()
        
        def get_adjacents(r: int, c: int):
            if r > 0:
                yield (r - 1, c)
            if c > 0:
                yield (r, c - 1)
            if r < ROWS - 1:
                yield (r + 1, c)
            if c < COLS - 1:
                yield (r, c + 1)
                
        def find(r: int, c: int, trie: TrieNode, visited: set):
            if not trie:
                return
            if trie.word:
                nonlocal found
                found.add(trie.word)
                trie.prune()
            visited.add((r, c))
            for nr, nc in get_adjacents(r, c):
                next_char = board[nr][nc]
                if (nr, nc) not in visited and next_char in trie.nexts:
                    find(nr, nc, trie.nexts[next_char], visited)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                find(r, c, trie_root.nexts.get(char), set())
                
        return found