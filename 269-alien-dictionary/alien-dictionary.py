from dataclasses import dataclass

@dataclass
class TrieNode:
    c: chr
    children: dict["TrieNode"]
    children_order: List[chr]
    is_word: bool

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        we can construct a trie with each node containing a list of characters
        within each list, the characters will be allegedly sorted lexicographically
        construct a topology and sort
        """
        
        followers = defaultdict(set)
        indegrees = {c: 0 for word in words for c in word }
        leaves = set() 
        chars = set()

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in followers[c]:
                        followers[c].add(d)
                        indegrees[d] += 1
                    break
            else: 
                if len(second_word) < len(first_word): 
                    return ""

        frontier = deque([c for c in indegrees if indegrees[c] == 0])
        result = []

        while frontier:
            c = frontier.popleft()
            result.append(c)
            for y in followers[c]:
                indegrees[y] -= 1
                if indegrees[y] == 0:
                    frontier.append(y)
        
        if len(result) < len(indegrees):
            return ""

        return "".join(result)
