# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node: Optional[ListNode]) -> ListNode:
            if not node or not node.next:
                return node
            old_next = node.next
            node.next = None
            reversed_head = reverse(old_next)
            old_next.next = node
            
            return reversed_head
        
        def compare(h1: ListNode, h2: ListNode) -> bool:
            while h1 and h2:
                if h1.val != h2.val:
                    return False
                h1 = h1.next
                h2 = h2.next
            
            return not h1 and not h2
        
        sentry = ListNode(next=head)
        slow_prev, slow, quick = sentry, head, head.next
        while slow:
            if not quick: # odd
                right_half_reversed = reverse(slow.next)
                slow_prev.next = None
                return compare(sentry.next, right_half_reversed)
            if not quick.next: # even
                right_half_reversed = reverse(slow.next)
                slow.next = None
                return compare(sentry.next, right_half_reversed)
            slow_prev = slow
            slow = slow.next
            quick = quick.next.next
        
        return False