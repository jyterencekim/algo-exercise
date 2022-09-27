# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentry = merged = ListNode()
        
        candidates = PriorityQueue()
        for node in lists:
            if node:
                candidates.put((node.val, hash(node), node))
        
        while not candidates.empty():
            v, _, node = candidates.get()
            merged.next = ListNode(val=v)
            merged = merged.next
            if node.next:
                candidates.put((node.next.val, hash(node.next), node.next))
        
        return sentry.next
        