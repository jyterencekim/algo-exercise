"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # (original node, blank clone) -> set blank clone's value upon visit
        if not root:
            return None
        clone_root = Node(root.val)
        q = deque([(root, clone_root)])
        
        while q:
            original, clone = q.popleft()
            
            for child in original.children:
                clone_child = Node(child.val)
                clone.children.append(clone_child)
                q.append((child, clone_child))
        
        return clone_root
        