# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_head = odd = odd_tail = head
        even_head = even = head.next
        
        while odd:
            even = odd.next
            if even:
                odd.next = even.next 
                even.next = even.next.next if even.next else None
            if not odd.next:
                odd.next = even_head
                break
            odd = odd.next
        
        return odd_head
                
            