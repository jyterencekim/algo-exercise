# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sentry = ListNode()
        l = head
        r = head
        r_prevs = []
        n = 1
        while r.next:
            n += 1
            r_prevs.append(r)
            r = r.next
        
        ptr = sentry
        take_l = True
        for i in range(n):
            if take_l:
                ptr.next = l
                ptr = l
                l = l.next
            else:
                ptr.next = r
                ptr = r
                r = r_prevs.pop()
            ptr.next = None
            take_l = not take_l

        return sentry.next
