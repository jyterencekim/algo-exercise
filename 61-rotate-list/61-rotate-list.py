# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length(node: Optional[ListNode]) -> int:
            if not node:
                return 0
            return 1 + get_length(node.next)
        
        if not head:
            return head
        
        N = get_length(head)
        k = k % N
        
        if not k:
            return head
        
        slow = sentry = ListNode(val=None, next=head)
        fast = slow
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # slow.next is pointing at the new rotated list's head
        # and fast is the last element that now must point to the old head
        fast.next = sentry.next
        sentry.next = slow.next
        slow.next = None
        
        return sentry.next
        
        