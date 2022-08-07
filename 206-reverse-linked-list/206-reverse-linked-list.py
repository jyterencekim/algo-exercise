# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:
            if not node or not node.next:
                return node
            
            old_next = node.next
            reversed_head = reverse(old_next)
            old_next.next = node
            node.next = None
            
            return reversed_head
        
        return reverse(head)
            
            