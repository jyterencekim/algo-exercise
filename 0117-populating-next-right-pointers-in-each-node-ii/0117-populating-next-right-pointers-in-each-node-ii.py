"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque()
        q.append((root, 0))
        level = 0
        prev = None
        
        while q:
            curr, curr_level = q.popleft()
            if curr_level > level:
                prev = None
                level = curr_level
            if prev:
                prev.next = curr
            prev = curr
            if curr.left:
                q.append((curr.left, curr_level + 1))
            if curr.right:
                q.append((curr.right, curr_level + 1))
                
        return root
        