# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_pre_middle(head: Optional[ListNode]) -> Optional[ListNode]:
            slow, quick = head, head.next
            proceed_slow = False

            while quick and quick.next:
                quick = quick.next
                if proceed_slow:
                    slow = slow.next
                proceed_slow = not proceed_slow
            
            return slow

        pre_middle = get_pre_middle(head)
        middle = pre_middle.next
        if not middle:
            return None
        post_middle = middle.next
        pre_middle.next = post_middle
        
        return head