# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        def do_reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            """
            return the head of the first reversed portion
            """
            if not head:
                return None
            
            remaining = k
            probe = head
            while remaining and probe:
                remaining -= 1
                probe = probe.next
            
            if remaining and not probe:
                # short of k
                return head 
            
            remaining = k
            prev = None
            curr = head
            while remaining:    
                remaining -= 1
                original_curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = original_curr_next
            
            # at this point, curr must be the remaining portion's head
            next_head = curr
            reversed_head = prev
            reversed_tail = head
            
            reversed_tail.next = do_reverse(next_head)
            return reversed_head
        
        return do_reverse(head)
        
            