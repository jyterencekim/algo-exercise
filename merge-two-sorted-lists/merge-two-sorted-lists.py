# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentry = current = ListNode()
        
        while list1 or list2:
            x = list1.val if list1 else math.inf
            y = list2.val if list2 else math.inf
            if x <= y:
                current.next = ListNode(val=x)
                list1 = list1.next
            else:
                current.next = ListNode(val=y)
                list2 = list2.next
            current = current.next
        
        return sentry.next