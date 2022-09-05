# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentry = ListNode(next=head)
        
        length = 0
        p = sentry
        while p.next:
            length += 1
            p = p.next
        
        target = length - n + 1
        p = sentry
        for x in range(target - 1):
            p = p.next
        p.next = p.next.next
        
        return sentry.next
        