# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode], prev: ListNode) -> Optional[ListNode]:
            if not node:
                return prev
            
            reversed_head = reverse(node.next, node)
            node.next = prev
            return reversed_head
        
        return reverse(head, None)
            
            