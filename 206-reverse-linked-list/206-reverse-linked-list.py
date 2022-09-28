# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            if not node.next:
                return node
            new_tail = node.next
            new_head = reverse(node.next)
            new_tail.next = node
            node.next = None
            return new_head
        return reverse(head)
        
        