# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        sentry = ListNode(next=head)
        
        behind = sentry
        ahead = head.next if head else None
        
        while ahead:
            tail_next = ahead.next
            tail = behind.next
            behind.next = ahead
            ahead.next = tail
            tail.next = tail_next
            
            behind = tail
            ahead = tail_next.next if tail_next else None
        
        return sentry.next
        
        