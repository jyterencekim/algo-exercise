# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentry = merged = ListNode()
        if not lists:
            return None
        min_heap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, idx))
        
        while min_heap:
            min_val, min_idx = heapq.heappop(min_heap)
            next_to_push = lists[min_idx].next
            lists[min_idx] = next_to_push
            if next_to_push:
                heapq.heappush(min_heap, (next_to_push.val, min_idx))
            merged.next = ListNode(min_val)
            merged = merged.next
        
        return sentry.next