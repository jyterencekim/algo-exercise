# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentry = ListNode(val=0, next=head)
        curr = sentry
        left_prev = None
        left = curr
        right_prev = None
        right = None
        
        for i in range(k):
            left_prev = curr
            curr = curr.next
            
        # now curr is at kth node from the beginning
        left = curr 
        
        right_curr = sentry
        while curr:
            right_prev = right_curr
            right_curr = right_curr.next
            curr = curr.next
        
        # now right_curr is at kth node from the end
        right = right_curr
        
        # swap
        left_prev.next = right
        right_prev.next = left
        right.next, left.next = left.next, right.next
        
        return sentry.next
        