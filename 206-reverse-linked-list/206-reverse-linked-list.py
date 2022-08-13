# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        sentry = curr = ListNode()
        while stack:
            popped = stack.pop()
            curr.next = popped
            curr = curr.next
            popped.next = None
            
        return sentry.next
        