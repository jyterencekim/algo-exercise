"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        clone_head = Node(node.val)
        
        q = deque()
        q.append((node, clone_head))
        
        clones = dict()
        clones[clone_head.val] = clone_head
        visited = set()
        
        while q:
            original, clone = q.popleft()
            
            for nei in original.neighbors:
                clone_nei = clones.get(nei.val, Node(nei.val))
                clone.neighbors.append(clone_nei)
                if nei.val not in clones:
                    clones[nei.val] = clone_nei
                    q.append((nei, clone_nei))
        
        return clone_head
            
        
        