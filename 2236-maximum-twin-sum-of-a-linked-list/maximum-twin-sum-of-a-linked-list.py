# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def to_list(head: Optional[ListNode]) -> List[int]:
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return result
        
        lst = to_list(head)
        N = len(lst)
        return max([x + y for x, y in zip(lst[:N//2], lst[N-1:N//2-1:-1])])