# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(x: Optional[ListNode], y: Optional[ListNode]) -> Optional[ListNode]:
            sentry = ListNode()
            pt = sentry
            while x and y:
                if x.val < y.val:
                    pt.next = x
                    x = x.next
                else:
                    pt.next = y
                    y = y.next
                pt = pt.next
            pt.next = x or y
            return sentry.next
        
        def divide(x: Optional[ListNode]) -> Tuple[Optional[ListNode]]:
            if not x:
                return x
            
            prev = None
            pt = x
            while pt and pt.next:
                prev = prev.next if prev else x
                pt = pt.next.next
            
            mid = prev.next
            prev.next = None
            return x, mid
        
        if not head or not head.next:
            return head
        
        left_head, right_head = divide(head)
        l, r = self.sortList(left_head), self.sortList(right_head)
        return merge(l, r)
            
            
            
            
                