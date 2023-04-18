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
                val = None
                if x.val < y.val:
                    val = x.val
                    next_x = x.next
                    x.next = None
                    pt.next = x
                    x = next_x
                else:
                    val = y.val
                    next_y = y.next
                    y.next = None
                    pt.next = y
                    y = next_y
                pt = pt.next
            if x:
                pt.next = x
            elif y:
                pt.next = y
            
            return sentry.next
        
        def divide(x: Optional[ListNode]) -> Tuple[Optional[ListNode]]:
            if not x:
                return x
            
            a = b = x
            a_prev = None
            a_goes = True
            # x ... a_prev (a = mid) .. b - None
            
            while b.next:
                a_prev = a
                if a_goes:
                    a = a.next
                a_goes = not a_goes
                b = b.next
            
            right_head = a_prev.next
            a_prev.next = None
            return x, right_head
        
        if not head or not head.next:
            return head
        
        left_head, right_head = divide(head)
        l, r = self.sortList(left_head), self.sortList(right_head)
        return merge(l, r)
            
            
            
            
                