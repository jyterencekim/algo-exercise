# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max_sum(node: Optional[TreeNode]) -> Tuple[int]:
            # returns (connectable, not connectable)
            if not node:
                return -math.inf, -math.inf
            
            left, left_unconnectable = get_max_sum(node.left)
            right, right_unconnectable = get_max_sum(node.right)
            center = node.val
            
            sum_unconnectable = max(left + center + right, left_unconnectable, right_unconnectable, left, right)
            sum_connectable = max(left + center, center + right, center)
            
            return sum_connectable, sum_unconnectable
        
        return max(get_max_sum(root))
            