# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def take_root(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], take_root(lo, mid - 1), take_root(mid + 1, hi))
        
        return take_root(0, len(nums) - 1)