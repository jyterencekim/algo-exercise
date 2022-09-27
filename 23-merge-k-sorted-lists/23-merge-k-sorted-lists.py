# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def do_merge(ls: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not ls:
                return None
            if len(ls) == 1:
                return ls[0]
            if len(ls) == 2:
                curr = sentry = ListNode()
                x, y = ls[0], ls[1]
                
                while x or y:
                    val_x = x.val if x else math.inf
                    val_y = y.val if y else math.inf
                    
                    if val_x <= val_y:
                        curr.next = ListNode(val=val_x)
                        x = x.next
                    else:
                        curr.next = ListNode(val=val_y)
                        y = y.next
                        
                    curr = curr.next
                
                return sentry.next
            
            mid = len(ls) // 2
            left, right = do_merge(ls[:mid]), do_merge(ls[mid:])
            return do_merge([left, right])
        
        return do_merge(lists)
                