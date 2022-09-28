# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:
            if not node:
                return None, None
            if not node.next:
                return node, node
            
            new_head, sub_tail = reverse(node.next)
            sub_tail.next = node
            node.next = None
            return new_head, node
        
        slow = sentry = ListNode(val=None, next=head)
        fast = slow
        for _ in range(k):
            fast = fast.next
        
        # k-group -> slow (... fast) ...
        while fast:
            next_to_go = fast.next
            fast.next = None # disconnect temporarily
            
            new_head, new_tail = reverse(slow.next)
            
            slow.next = new_head
            new_tail.next = next_to_go
            slow = new_tail
            fast = slow
            for _ in range(k):
                fast = fast.next if fast else None
        
        return sentry.next