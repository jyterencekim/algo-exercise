"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # original -> id -> copy
        original_to_copy = dict()
        
        sentry = curr = Node(0)
        idx = 0
        reader = head
        while reader:
            curr.next = Node(reader.val)
            curr = curr.next
            original_to_copy[reader] = curr
            reader = reader.next
            
        reader = head
        curr = sentry.next
        while reader:
            curr.random = original_to_copy[reader.random] if reader.random else None
            reader = reader.next
            curr = curr.next
        
        return sentry.next