# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentry = ListNode()
        sentry.next = head
        
        """
        1 [2 3 4] 5
        
        1<-2<-3<-4->5
        1 2<-3<-4->5 
          2 -----> 5
        1 -> 4 -> 3 -> 2 -> 5
          
        """
        if left == right:
            return head
        
        def reverse(node: ListNode, prev: ListNode, acc: int) -> Tuple[ListNode]: 
            # head of the reversed portion and the new tail (normal right)
            original_next = node.next
            node.next = prev
            if acc == right or not original_next:
                return node, original_next
            return reverse(original_next, node, acc + 1)
            
        def traverse(node: ListNode, prev: ListNode, acc: int):
            if not node or not node.next:
                return
            if acc == left:
                left_normal = prev
                reversed_tail = node
                
                reversed_head, normal_right = reverse(node.next, node, acc + 1)
                reversed_tail.next = normal_right
                left_normal.next = reversed_head
            else:
                traverse(node.next, node, acc + 1)
        
        traverse(sentry, None, 0)
        return sentry.next
                
                
                