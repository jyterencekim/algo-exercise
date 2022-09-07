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
        even_head = even = None
        
        while odd:
            even = odd.next
            if not even_head:
                even_head = even
            odd.next = even.next if even else None
            if even:
                even.next = even.next.next if even.next else None
            odd_tail = odd
            odd = odd.next
        
        odd_tail.next = even_head
        
        return odd_head
                
            