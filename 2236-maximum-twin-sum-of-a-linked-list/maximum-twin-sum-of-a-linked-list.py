# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def get_halfpoint(head: Optional[ListNode]) -> Optional[ListNode]:
            """
            returns the node right before the second half
            """
            slow, quick = head, head
            proceed_slow = False
            while quick.next:
                quick = quick.next
                if proceed_slow:
                    slow = slow.next
                proceed_slow = not proceed_slow
            return slow 

        def reverse(head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not head.next:
                head.next = prev
                return head
            next_node = head.next
            head.next = prev
            return reverse(next_node, head)
        
        # separate the two parts
        halfpoint = get_halfpoint(head)
        x = head
        y = halfpoint.next
        halfpoint.next = None

        y = reverse(y, None)

        max_pair_sum = 0
        while x and y:
            pair_sum = x.val + y.val
            max_pair_sum = max(max_pair_sum, pair_sum)
            x = x.next
            y = y.next
        
        return max_pair_sum


