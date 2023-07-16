END = '#'

class MagicDictionary:

    def __init__(self):
        self.trie = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            pt = self.trie
            for c in word:
                if c not in pt:
                    pt[c] = dict()
                pt = pt[c]
            pt[END] = {}
    
    def probe(self, target: str, pt: int, trie_pt: dict, tolerated=0) -> bool:
        if not trie_pt:
            return False
        if tolerated > 1:
            return False
        if pt == len(target):
            return END in trie_pt and tolerated == 1
        
        return any(self.probe(target, pt + 1, trie_pt[c], tolerated + (target[pt] != c)) for c in trie_pt)
        

    def search(self, searchWord: str) -> bool:
        return self.probe(searchWord, 0, self.trie)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)