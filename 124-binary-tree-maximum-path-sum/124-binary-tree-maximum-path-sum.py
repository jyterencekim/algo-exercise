# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max_sum = -math.inf
        
        def get_max_sum(node: Optional[TreeNode]) -> Tuple[int]:
            if not node:
                return 0
            
            left = get_max_sum(node.left)
            right = get_max_sum(node.right)
            center = node.val
            
            sum_through_node = left + center + right
            sum_with_child = max(left + center, center + right)
            sum_alone = center
            
            nonlocal global_max_sum
            global_max_sum = max(global_max_sum, sum_through_node, sum_with_child, sum_alone)
            
            return max(sum_with_child, sum_alone)
        
        get_max_sum(root)
        return global_max_sum
            